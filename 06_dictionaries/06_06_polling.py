poll_taken = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python'
}

poll_takers = {
    'britan' : 'python',
    'mark' : 'c++',
    'edward' : 'rust',
    'jarred' : 'java'
}

for name in poll_takers:
    if poll_taken.get(name):
        print(f'Sorry {name.title()}, you have already responded to this poll.')
    else:
        print(f'Hello {name.title()}! Please take this poll.')
