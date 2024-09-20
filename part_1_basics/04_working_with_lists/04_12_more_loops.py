# Lists from the book from file "foods.py"
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

# Print all items in the list
for food in my_foods:
    print(food.title())

print('----------------------')

# Print the first three items in the list
for index in range(0, 3):
    print(my_foods[index].title())