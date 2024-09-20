poll = {}
poll_active = True

while poll_active:
    
    print("\nWelcome to the Dream Vacation Poll!")
    answer = input('Would you like to start a poll? (y/n): ').strip().lower()

    if answer == 'y':
        while True:
            name = input('\nWhat is your name? ').strip()
            poll_answer = input('Where is your dream vacation? ').strip()
            poll[name] = poll_answer
            
            print(f'\nCurrent responses: {len(poll)}')

            add_response_continue = input('Would you like to add another response? (y/n): ').strip().lower()
            if add_response_continue == 'y':
                continue
            if add_response_continue == 'n':
                poll_active = False
                break
             
    elif answer == 'n':
        print('Ending Program')
        poll_active = False

print("\n===================================")
print("           Poll Results            ")
print("===================================")
if poll:
    for name, vacation in poll.items():
        print(f"{name}'s dream vacation is {vacation}.")
else:
    print("No responses were collected.")

print("===================================")
print("       Thank you for voting!   ")
print("===================================")
