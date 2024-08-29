#Enter your name
name = input("Enter your name")
print(name)
#Enter three numbers
numbers = []
even_odd = []
for i in range(0,3):
    num = int(input(f"Enter your {i+1}st favorite number:"))
    numbers.append(num)
    print(numbers[0])
    if numbers[i] % 2 == 0:
              status = 'even'
    else:
              status = 'odd'    
    even_odd.append((num, status))
#save number and even/odd status in a tuple
for item in even_odd:
    num, status = item
    print(f"The number {num} is {status}.")
#square of the numbers
for num in numbers:
    square_tuple = (num, num**2)
    print(f'The number {num} and its square: {square_tuple}')
sum_num = sum(numbers)
print(f'Amazing! The sum of your favorite numbers is: {sum_num}')
#prime number
if sum_num % 2 != 0:
    print(f'Wow, {sum_num} is a prime number!')
else:
    print(f"{sum_num} is not a prime number")







