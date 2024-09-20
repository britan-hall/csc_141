prompt = '\nWhat toppings would you like added to your pizza?'
prompt += '\nIf none, enter "quit" to exit. '

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f'Adding {topping} to your pizza!')