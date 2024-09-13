def make_sandwich(*items):
    print('\nMaking your sandwich with:')
    for item in items:
        print(f'- {item.title()}')

make_sandwich('cheese','pastrami','lettuce')
make_sandwich('bread')
make_sandwich('tomatoe','bacon')