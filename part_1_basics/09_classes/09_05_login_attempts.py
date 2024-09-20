class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f'User: {self.first_name} {self.last_name}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


user = Users('Britan','Hall')

for i in range (0,50):
    user.increment_login_attempts()
print(f'Login Attempts: {user.login_attempts}')

user.reset_login_attempts()
print(f'Login Attempts: {user.login_attempts}')