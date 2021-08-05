"""
Write a program that will calculate the result of the given operation
(adding, subtracting, multiplying, dividing) based on the two numbers given.
If an incorrect operation is specified, the program should
display an appropriate error message.

Sample program output:
Enter the first number: 10
Enter the second number: 5
Enter the type of operation (+, -, *, /): +
Result: 15
"""

number_1 = float(input('Enter the first number: '))
number_2 = float(input('Enter the second number: '))
operation = input('Enter the type of operation (+, -, *, /): ')

if operation == '+':
    print(number_1 + number_2)
elif operation == '-':
    print(number_1 - number_2)
elif operation == '*':
    print(number_1 * number_2)
elif operation == '/':
    print(number_1 / number_2)
else:
    print('invalid operator')