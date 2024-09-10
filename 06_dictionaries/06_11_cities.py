# Creating the dictionary with city information
cities = {
    "New York": {
        "country": "USA",
        "population": 8419000,
        "fact": "New York City is known as 'The City That Never Sleeps'."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 13960000,
        "fact": "Tokyo is the most populated city in the world."
    },
    "Paris": {
        "country": "France",
        "population": 2148000,
        "fact": "Paris is known as 'The City of Light'."
    }
}

for city_name, info in cities.items():
    for city in city_name:
        country = info['country']
        population = info['population']
        fact = info['fact']
    print(city_name)
    print(f'\tCountry: {country}')
    print(f'\tPopulation: {population}')
    print(f'\tFun Fact: {fact}')

