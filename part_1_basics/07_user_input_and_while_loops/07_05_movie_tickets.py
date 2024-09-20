while True:
    age = int(input('\nWhat is your age?\nEnter "999" to exit '))
    
    if age == 999:
        break
    if age < 3:
        print('Your ticket is free!')
    if age >= 3:
        if age < 12:
            print('Your ticket is $10.')
    if age >= 12:
        print('Your ticket is $15.')