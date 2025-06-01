import unittest
from unittest.mock import patch, MagicMock
import calculator_agent # Assuming calculator_agent.py is in the same directory or PYTHONPATH

# Mock the OpenAI client before it's used by calculator_agent
# This is important if calculator_agent.py initializes client at the module level.
# We need to mock it BEFORE calculator_agent is imported for the first time in a test context.
mock_openai_client = MagicMock()

# If calculator_agent.py initializes client like `client = openai.OpenAI()` at module level:
# We patch 'openai.OpenAI' to return our mock_openai_client when it's called.
# This way, when calculator_agent.py runs its `client = openai.OpenAI()`, it gets our mock.
module_patch = patch('openai.OpenAI', return_value=mock_openai_client)
module_patch.start() # Start the patch before calculator_agent is potentially imported by test runner

# Now it's safer to import calculator_agent, as its attempt to create an openai.OpenAI() client
# will use our mock.
import calculator_agent

class TestCalculatorAgent(unittest.TestCase):

    def setUp(self):
        # Reset the mock for each test to ensure independence
        mock_openai_client.reset_mock()

        # Ensure the global 'client' in calculator_agent is our mock_openai_client
        # This is because the calculator_agent directly uses a global 'client'
        calculator_agent.client = mock_openai_client

    @classmethod
    def tearDownClass(cls):
        # Stop the patch after all tests in the class are done
        module_patch.stop()

    def test_valid_expression_and_mocked_ai(self):
        expression = "2 + 2"
        expected_correct_answer = 4
        mock_ai_fake_answer = "5" # What our mocked AI will return

        # Configure the mock client's behavior for this test
        mock_completion = MagicMock()
        mock_completion.choices = [MagicMock()]
        mock_completion.choices[0].message = MagicMock()
        mock_completion.choices[0].message.content = mock_ai_fake_answer
        mock_openai_client.chat.completions.create.return_value = mock_completion

        correct, fake, error = calculator_agent.calculator_agent(expression)

        self.assertEqual(correct, expected_correct_answer)
        self.assertEqual(fake, mock_ai_fake_answer)
        self.assertIsNone(error)
        mock_openai_client.chat.completions.create.assert_called_once()

    def test_expression_with_eval_error(self):
        expression = "10 / 0" # Division by zero
        mock_ai_fake_answer = "Some fake answer for division by zero"

        # Configure the mock client
        mock_completion = MagicMock()
        mock_completion.choices = [MagicMock()]
        mock_completion.choices[0].message = MagicMock()
        mock_completion.choices[0].message.content = mock_ai_fake_answer
        mock_openai_client.chat.completions.create.return_value = mock_completion

        correct, fake, error = calculator_agent.calculator_agent(expression)

        self.assertIsNone(correct) # Correct answer should be None due to error
        self.assertEqual(fake, mock_ai_fake_answer)
        self.assertIsNotNone(error)
        self.assertIn("division by zero", error.lower()) # Check for specific error message
        mock_openai_client.chat.completions.create.assert_called_once() # AI should still be called

    def test_openai_api_error(self):
        expression = "1 + 1"
        expected_correct_answer = 2

        # Simulate an API error
        mock_openai_client.chat.completions.create.side_effect = calculator_agent.openai.APIError("Test API Error", request=None, body=None, code=None, headers=None)

        correct, fake, error = calculator_agent.calculator_agent(expression)

        self.assertEqual(correct, expected_correct_answer)
        self.assertEqual(fake, "Could not generate a fake answer.") # Default message
        self.assertIsNotNone(error)
        self.assertIn("Test API Error", error)
        mock_openai_client.chat.completions.create.assert_called_once()

    def test_invalid_expression_no_eval(self):
        expression = "invalid expression"
        mock_ai_fake_answer = "fake answer for invalid"

        # Configure the mock client
        mock_completion = MagicMock()
        mock_completion.choices = [MagicMock()]
        mock_completion.choices[0].message = MagicMock()
        mock_completion.choices[0].message.content = mock_ai_fake_answer
        mock_openai_client.chat.completions.create.return_value = mock_completion

        correct, fake, error = calculator_agent.calculator_agent(expression)

        self.assertIsNone(correct)
        self.assertEqual(fake, mock_ai_fake_answer)
        self.assertIsNotNone(error)
        self.assertIn("invalid expression", error.lower()) # Check for specific error message
        mock_openai_client.chat.completions.create.assert_called_once()


if __name__ == "__main__":
    unittest.main()
