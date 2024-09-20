favorite_numbers = {
    'Britan': [1,2,3],
    'Mark' : [19,22,32],
    'Jarred' : [21,72,93],
    'Lewis' : [77,93,2035],
    'Parker' : [87,34,89]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(number)