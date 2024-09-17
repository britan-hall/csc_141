class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f'User: {self.first_name} {self.last_name}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')

class Admin:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = Privileges()

    def describe_admin(self):
        print(f'Admin: {self.first_name} {self.last_name}')

    def greet_admin(self):
        print(f'Hello {self.first_name} {self.last_name}!')

class Privileges():

    def __init__(self):
        self.privileges = ['can make post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Admin Privileges:')
        for privilege in self.privileges:
            print(privilege)

