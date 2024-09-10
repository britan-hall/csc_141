pet_1 = {
    'animal' : 'dog',
    'owner' : 'joe'
}

pet_2 = {
    'animal' : 'cat',
    'owner' : 'susan'
}

pet_3 = {
    'animal' : 'fish',
    'owner' : 'kelly'
}

pets = [pet_1,pet_2,pet_3]

for pet in pets:
    for k,v in pet.items():
        animal_type = pet['animal']
        owner_name = pet['owner']

    print(f'\nAnimal: {animal_type.title()}')
    print(f'Owner: {owner_name.title()}')
    