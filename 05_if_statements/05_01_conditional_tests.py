car = 'audi'

print('\nIs car == "audi"? I predict True.')
print(car == 'audi')

print('\nIs car == "mercedes"? I predict False.')
print(car == 'mercedes')

print('\nIs car == "Audi"? I predict False.')
print(car == 'Audi')

print('\nIs car.title() == "Audi"? I predict True.')
print(car.title() == 'Audi')

num_1 = 21

print('\nIs num_1 == 12? I predict False.')
print(num_1 == 12)

print('\nIs num_1 == 21? I predict True.')
print(num_1 == 21)

print('\nIs num_1 < 100? I predict True.')
print(num_1 < 100)

print('\nIs num_1 < 10? I predict False.')
print(num_1 < 10)

print('\nIs num_1 > 20 AND num_1 < 22? I predict True.')
print((num_1 > 20) and (num_1 < 22))

print('\nIs num_1 > 20 AND num_1 > 22? I predict False.')
print((num_1 > 20) and (num_1 > 22))
