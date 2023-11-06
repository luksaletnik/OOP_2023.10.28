number1 = float(input('Enter the number 1: '))
number2 = float(input('Enter the number 2: '))

try:
    result = number1 / number2
    print(f'The result of division {number1} by {number2} is: {result}')
except ZeroDivisionError:
    result = 0
    print('Division by zero is impossible')

    print('The next part of the program')
