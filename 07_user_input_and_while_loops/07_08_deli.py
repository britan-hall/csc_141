sandwich_orders = [
                    "Grilled Cheese",
                    "BLT",
                    "Turkey Club",
                    "Reuben",
                    "Caprese"
                ]   

finished_sandwiches = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        print('\n------------------------------')
        print(f'Making a {sandwich} now.')
        print('------------------------------')
        finished_sandwiches.append(sandwich)
        sandwich_orders.remove(sandwich)

print('\nAll sandwich orders have been filled. Here is the list of filled orders:')
for sandwich in finished_sandwiches:
    print(f'- {sandwich}')