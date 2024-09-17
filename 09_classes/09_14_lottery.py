from random import choice

combo_tulpe = (0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e')
made_combo = []

def make_combo():
    for i in range (1,6):
        pick = choice(combo_tulpe)
        made_combo.append(pick)
    return made_combo

print(f'Winning lottery code: {make_combo()}')