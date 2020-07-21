# fahrenheit = input('What is the temperature in fahrenheit? ')
# celsius = 0.0
# if fahrenheit.isnumeric() == True:
#     celsius = (fahrenheit - 32) * 5/9
# else:
#     print('Input is not a number.')
#     exit()
# print('Temperature in celsius is', int(celsius))

operations = ['+', '-', '*', '/', '%', '^']

print("Simple calculator!")
first_value = input('First Number: ')
second_value = input('Second Number: ')
if first_value.isnumeric() == False or second_value.isnumeric() == False:
    print('Input is not a number.')
    exit()

operator = input('Operation? ')
if operator not in operations:
    print('Operation not recognized.')
    exit()

if operator == '+':
    sum = int(first_value) + int(second_value)
    print('bla bla bla', sum)
if operator == '-':
    sub = int(first_value) - int(second_value)
    print('bla bla bla', sub)
if operator == '*':
    mut = int(first_value) * int(second_value)
    print('bla bla bla', mut)
if operator == '/':
    div = int(first_value) / int(second_value)
    print('bla bla bla', div)
if operator == '%':
    mod = int(first_value) % int(second_value)
    print('bla bla bla', mod)
if operator == '^':
    exp = int(first_value) * int(second_value)
    print('bla bla bla', exp)

    print('Simple calculator!')

first_number = input('First number? ')

if first_number.isnumeric() == False:
    print('Please input a number.')
    exit()

operation = input('Operation? ')

second_number = input('Second number? ')

if second_number.isnumeric() == False:
    print('Please input a number.')
    exit()

first_number = int(first_number)
second_number = int(second_number)

result = 0
if operation == '+':
    result = first_number + second_number
    label = 'sum'
elif operation == '-':
    result = first_number - second_number
    label = 'difference'
elif operation == '*':
    result = first_number * second_number
    label = 'product'
elif operation == '/':
    result = first_number / second_number
    label = 'quotient'
elif operation == '**':
    result = first_number ** second_number
    label = 'exponent'
elif operation == '%':
    result = first_number % second_number
    label = 'modulus'
else:
    print('Operation not recognized.')
    exit()

print(label + ' of ' + str(first_number) + ' ' + operation + ' ' + str(second_number) + ' equals ' + str(result))