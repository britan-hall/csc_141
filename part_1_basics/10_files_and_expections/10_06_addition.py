# 2, simple function that handles errors

def addition():
    while True:
        number_1 = input('Enter a number: ')
        try:
            number_1 = int(number_1)
            break  
        except ValueError:
            print('Error: Please enter a valid number!')

    while True:
        number_2 = input('Enter a second number: ')
        try:
            number_2 = int(number_2)
            break 
        except ValueError:
            print('Error: Please enter a valid number!')

    print(f'The sum of your numbers is: {number_1 + number_2}')

addition()
