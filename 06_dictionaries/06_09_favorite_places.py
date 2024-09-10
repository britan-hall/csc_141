favorite_places = {
    'Britan' : ['Bernville', 'Reading', 'Coasta Rica'],
    'Mark' : ['Bethel', 'Alaska'],
    'Jarred' : ['Tulpehocken', 'Bernville']
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places:")
    for place in places:
        print(f'\t{place}')