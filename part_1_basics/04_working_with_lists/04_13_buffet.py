# Original tuple
menu_items = ('burger', 'fries', 'chicken nuggets', 'salad', 'noodles')

# Print the original items
print("Original Menu Items:")
for item in menu_items: 
    print(item.title())

# Attempting to change an item in the tuple (This will cause an error)
# menu_items[0] = 'hamburger'

# Modify tuple , changing 'burger' to 'hamburger' and 'fries' to 'french fries'
menu_items = ('hamburger', 'french fries', 'chicken nuggets', 'salad', 'noodles')

print('-----------------')
print("Modified Menu Items:")
for item in menu_items: 
    print(item.title())