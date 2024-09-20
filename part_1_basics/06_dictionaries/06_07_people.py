person_1 = {
    'first_name' : 'Britan', 
    'last_name' : 'Hall',
    'age' : 17,
    'city' : 'Bernville',
}

person_2 = {
    'first_name': 'Avery',
    'last_name': 'Smith',
    'age': 22,
    'city': 'Ridgefield',
}

person_3 = {
    'first_name': 'Jordan',
    'last_name': 'Lee',
    'age': 29,
    'city': 'Lakeside',
}

people = [person_1,person_2,person_3]

for person in people:
    for k,v in person.items():
        full_name = f'{person['first_name']} {person['last_name']}'
        age = person['age']
        city = person['city']
    
    print(f'\n{full_name}')
    print(f'\tAge: {age}')
    print(f'\tCity: {city}')
    