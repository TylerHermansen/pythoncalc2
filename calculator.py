"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    data_input = input('Enter your equation ')
    token = data_input.split(' ')

    if 'q' in token:
        print('done')
        break

    elif len(token) < 2:
        print('Not enough inputs')
        continue

    operator = token[0]
    num1 = [1]

    if len(token) < 3:
        num2 = "0"
    
    else:
        num2 = token[2]
    
    if len(token) > 3:
        num3 = token [3]

    result = None

    if not num1.isdigit() or not num2.isdigit():
        print('Invalid numbers')
        continue

    if operator == '+':
        result = add(float(num1), float(num2))

    elif operator == '-':
        result = subtract(float(num1), float(num2))

    elif operator == '*':
        result = multiply(float(num1), float(num2))

    elif operator == '/':
        result = divide(float(num1), float(num2))

    elif operator == 'square':
        result = square(float(num1))
    
    elif operator == 'cube':
        result = cube(float(num1))
    
    elif operator == 'pow':
        result = power(float(num1), float(num2))

    elif operator == 'mod':
        result = mod(float(num1), float(num2))