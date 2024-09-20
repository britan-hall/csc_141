from random import randint

class Dice:
    def __init__(self, sides):
        self.sides = sides
   
    def roll_die(self, index):
        roll = randint(1, self.sides)
        print(f'Roll {index} for {self.sides}-sided die: {roll}')

die_6 = Dice(6)
for i in range(1,11):
    die_6.roll_die(i)
print('\n')

die_10 = Dice(10)
for i in range(1,11):
    die_10.roll_die(i)
print('\n')

die_20 = Dice(20)
for i in range(1,11):
    die_20.roll_die(i)
print('\n')