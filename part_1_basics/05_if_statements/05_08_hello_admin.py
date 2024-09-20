users = ['admin', 'britan', 'mark', 'jarred', "lewis"]

for users in users:
    if users == 'admin':
        print(f'Welcome back {users.upper()}. Would you like a status report?')
    else:
        print(f'Hello {users.title()}! Thank you for logging in.')