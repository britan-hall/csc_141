prompt = '\nWhat toppings would you like added to your pizza?'
prompt += '\nIf none, enter "quit" to exit. '
active = True
i = 0

while active == True:
    topping = input(prompt)
    if topping == 'quit':
        break
    elif i == 3:
        active = False
    else:
        print(f'Adding {topping} to your pizza!')
    i += 1