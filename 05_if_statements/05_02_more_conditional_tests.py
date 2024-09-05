# Tests for equailty and inequality in strings 
phrase = 'hotdog'
print(phrase.title() == 'Hotdog')
print(phrase == 'Hotdog')

# Tests using the lower() method
phrase_2 = "Cheeseburger"
print(phrase_2.lower() == 'cheeseburger')
print(phrase_2 == 'cheeseburger')

# Numerical Tests
num = 10
print(num > 9)
print(num < 9)
print(num >= 10)
print(num <= 9)

# 'and' / 'or' tests
keyword = 'hello'
number = 100
print((keyword == 'hello') and (number == 100))
print((keyword.upper() == 'hello') and (number == 100))
print((keyword.upper() == 'hello') or (number == 100))
print((keyword.upper() == 'hello') or (number == 10))

# Testing list items
list = ['Audi', 'BMW', 'Mercedes']
print('Audi' in list)
print('GMC' in list)
