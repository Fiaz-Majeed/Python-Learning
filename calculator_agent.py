import openai
import os

# It's recommended to set your OpenAI API key as an environment variable.
# For example, you can set OPENAI_API_KEY in your shell.
# If you haven't set it as an environment variable,
# you can uncomment the line below and replace "YOUR_API_KEY"
# with your actual API key.
# openai.api_key = "YOUR_API_KEY"

# Alternatively, ensure the OPENAI_API_KEY environment variable is set.
# If the API key is not set as an environment variable and also not directly in the code,
# the OpenAI library will raise an error.
try:
    client = openai.OpenAI()
    # You can remove the following print statement in the final version.
    print("OpenAI client initialized successfully.")
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    print("Please ensure your OpenAI API key is set correctly.")
    print("You can set it as an environment variable named OPENAI_API_KEY,")
    print("or by uncommenting the line `openai.api_key = "YOUR_API_KEY"`")
    print("in the `calculator_agent.py` file and replacing `"YOUR_API_KEY"` with your actual key.")


def calculator_agent(expression: str):
    """
    Takes a mathematical expression string, calculates the correct answer,
    and generates a fake answer using an AI model.

    Args:
        expression: The mathematical expression to evaluate (e.g., "2 + 2").

    Returns:
        A tuple containing:
            - The correct answer (float or int).
            - The fake answer (str).
            - An error message (str or None if no error).
    """
    global client # Assuming client is initialized globally in this file
    print(f"Received expression: {expression}")
    correct_answer = None
    ai_generated_fake_answer = "Could not generate a fake answer."
    error_message_calc = None
    error_message_ai = None

    try:
        # WARNING: eval() can be dangerous if the input is not trusted.
        correct_answer = eval(expression)
    except Exception as e:
        print(f"Error evaluating expression '{expression}': {e}")
        error_message_calc = f"Invalid expression for correct answer: {e}"

    try:
        # Ensure the client is available
        if 'client' not in globals() or client is None:
            raise openai.APIError("OpenAI client is not initialized.", request=None, body=None, code=None, headers=None)

        prompt = f"For the mathematical expression '{expression}', what is a plausible but definitely incorrect answer? Only provide the incorrect numerical answer, nothing else. For example, if the expression is '2+2', a plausible but incorrect answer could be '3' or '5'."

        # Using a standard model name. Replace 'gpt-3.5-turbo' if you have a specific model.
        # The issue mentioned "Gemini 2.0 flash". If this is accessible via OpenAI's API
        # under a different name, that name should be used here.
        # Otherwise, this uses a standard OpenAI model.
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo", # Replace with your desired model if different
            messages=[
                {"role": "system", "content": "You are an assistant that provides plausible but incorrect answers to mathematical expressions."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7, # Adjust for creativity
            max_tokens=10  # Expecting a short numerical answer
        )
        if completion.choices and completion.choices[0].message:
            ai_generated_fake_answer = completion.choices[0].message.content.strip()
        else:
            error_message_ai = "AI did not return a valid choice for the fake answer."

    except openai.APIError as e: # More specific error handling for OpenAI
        print(f"OpenAI API Error: {e}")
        error_message_ai = f"OpenAI API Error: {e}"
    except Exception as e:
        print(f"Error generating fake answer: {e}")
        error_message_ai = f"Error generating fake answer: {e}"

    # Combine error messages if any
    final_error_message = None
    if error_message_calc and error_message_ai:
        final_error_message = f"Calculation error: {error_message_calc}. AI error: {error_message_ai}"
    elif error_message_calc:
        final_error_message = error_message_calc
    elif error_message_ai:
        final_error_message = error_message_ai

    return correct_answer, ai_generated_fake_answer, final_error_message

if __name__ == "__main__":
    # Ensure your OPENAI_API_KEY is set as an environment variable or in the script.
    # If the client failed to initialize, the agent won't work correctly.
    if 'client' not in globals() or client is None:
        print("OpenAI client is not initialized. Please check your API key configuration.")
        print("Exiting example.")
    else:
        print("\n--- Calculator Agent Example ---")

        expressions_to_test = [
            "2 + 2",
            "10 * 5 - 3",
            "100 / 4",
            "7 * (3 + 2)",
            "2**5", # Power
            "10 / 0", # Division by zero (will cause eval error)
            "some nonsense" # Invalid expression (will cause eval error)
        ]

        for expr in expressions_to_test:
            print(f"\nTesting expression: \"{expr}\"")
            correct, fake, error = calculator_agent(expr)

            if error:
                print(f"  Error: {error}")

            # Even if there was an error in calculation, we might still have a fake answer.
            print(f"  Correct Answer: {correct}")
            print(f"  Fake Answer by AI: {fake}")

        print("\n--- Example End ---")
