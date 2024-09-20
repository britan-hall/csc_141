'''
Read about making fractions in Python
https://pymotw.com 

'''

import fractions

for numerator, demoninator in [(1, 2), (2, 4), (3, 6)]:
    fraction = fractions.Fraction(numerator, demoninator)
    print('{}/{} = {}'.format(numerator, demoninator, fraction))