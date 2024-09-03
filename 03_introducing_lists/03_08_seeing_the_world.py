places = ["greece", "paris", "london", "manchester", "bahamas"]

print("This is the original list:")
print(places)

print("This is the sorted list:")
print(sorted(places))

print("The orignial list wasn't changed:")
print(places)

print("This is the reverse sorted list:")
print((sorted(places, reverse=True)))

print("The orignial list wasn't changed:")
print(places)

print("This is the reversed list:")
places.reverse()
print(places)

print("You can get the original list back by using the reverse function again:")
places.reverse()
print(places)