current_users = ['britan', 'mark', 'jarred', 'lewis', 'austin']
new_users = ['calvin', 'lewis', 'vinny', 'parker', 'jarred']

for new_users in new_users:
    if new_users.lower() in current_users:
        print(f'The username {new_users.title()} is already in use. Please pick another one!')
    else:
        print(f'The username {new_users.title()} is avialable!')