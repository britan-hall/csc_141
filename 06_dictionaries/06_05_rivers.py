rivers = {
    'nile' : 'egpyt',
    'amazon' : 'south america',
    'rio grande' : 'united states'
}

# Loop to print out both keys and values in the dictionary
for k,v in rivers.items():
    print(f'The {k.title()} River is in {v.title()}.')
print('\n')

# Loop for each river in the dictionary
for river in rivers:
    print(river.title())
print('\n')

# Loop for each location in the dictionary
for value in rivers.values():
    print(value.title())