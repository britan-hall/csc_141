sandwich_orders = [
                    "Grilled Cheese",
                    "BLT",
                    "Pastrami",
                    "Turkey Club",
                    "Pastrami",
                    "Reuben",
                    "Pastrami",
                    "Caprese"
                ]   

finished_sandwiches = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        if sandwich == 'Pastrami':
            print('\n------------------------------')
            print('The deli has no more Pastrami!')
            print('------------------------------')
            while sandwich in sandwich_orders:
                sandwich_orders.remove(sandwich)
        else:
            print('\n------------------------------')
            print(f'Making a {sandwich} now.')
            print('------------------------------')
            finished_sandwiches.append(sandwich)
            sandwich_orders.remove(sandwich)

print('\nAll sandwich orders have been filled. Here is the list of filled orders:')
for sandwich in finished_sandwiches:
    print(f'- {sandwich}')