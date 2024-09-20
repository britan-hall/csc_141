from random import choice

combo_tulpe = (0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e')
made_combo = []
test_combo = []
attempts = 0

def make_combo():
    made_combo = []
    for i in range (1,4):
        pick = choice(combo_tulpe)
        made_combo.append(pick)
    return made_combo

winning_combo = make_combo()
print(f'Winning lottery combo: {winning_combo}')

def analysis(test_combo,attempts):
    while test_combo != winning_combo:
        test_combo = make_combo()
        print(f'Testing {test_combo} | Winning Combo {winning_combo}')
        attempts += 1
        make_combo()
    if test_combo == winning_combo:
        print(f'It took {attempts} attempts to get the same combo.')

analysis(test_combo,attempts)