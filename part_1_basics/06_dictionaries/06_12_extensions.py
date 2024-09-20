# code extented from the book's "pizza.py"

pizza = {
    'size': 'medium',
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', 'pepporoni'],
}

size = pizza['size'].capitalize()
crust = pizza['crust'].capitalize()
toppings = pizza['toppings']

print(f"Your pizza order:")
print(f"Size: {size}")
print(f"Crust: {crust}")
    
print(f"Toppings:")
for topping in toppings:
    print(f"\t- {topping.capitalize()}")

