



first_number = 0
second_number = 0
decision = "no"

def print_operations ():
    """This function shows you available operations"""
    print("""
    +
    -
    *
    /
    """)
def operation_on_numbers (operation_type, number_1, number_2):
    if operation_type == "+":
        print(f'{number_1} + {number_2} = {number_1 + number_2}')
        return number_1 + number_2
    elif operation_type == "-":
        print(f'{number_1} - {number_2} = {number_1 - number_2}')
        return number_1 - number_2
    elif operation_type == "*":
        print(f'{number_1} * {number_2} = {number_1 * number_2}')
        return number_1 * number_2
    elif operation_type == "/":
        print(f'{number_1} / {number_2} = {number_1 / number_2}')
        return number_1 / number_2


print('welcome to the Calculator app !')

while True:

    if first_number == 0 or decision == "n":
        first_number = int(input('Enter your first number: '))

    print_operations()

    operation_type = input('Pick an operation: ')

    second_number = int(input('Enter your second number: '))

    score = operation_on_numbers(operation_type, first_number, second_number)
    print(f'Score is: {score}')

    decision = input(f'Type \'y\' to continue calculating with {score}, or \'n\' to start a new calculation: ')
    if decision == 'y':
        first_number = score
    elif decision == 'n':
        continue
