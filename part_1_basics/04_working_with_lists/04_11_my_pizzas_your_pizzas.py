my_pizzas = ["pepperoni", "sausage", "ham"]
friend_pizzas = ["pepperoni", "sausage", "ham"]

my_pizzas.append('pineapple')
friend_pizzas.append('mushroom')

print()

print('My favorite types of pizza are:')
for my_pizzas in my_pizzas:
    print(f'{my_pizzas.title()}')

print()

print("My friend's favorite types of pizza are:")
for friend_pizzas in friend_pizzas:
    print(f'{friend_pizzas.title()}')