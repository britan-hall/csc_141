def city_country(city, country):
    message = (f"'{city.title()}, {country.title()}'")
    return message

message = city_country('New York', 'United States')
print(message)

message = city_country('Detriot', 'United States')
print(message)

message = city_country('London', 'England')
print(message)