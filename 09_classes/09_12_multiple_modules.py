from lib_09_12_multiple_modules_1 import Users
from lib_09_12_multiple_modules_2 import *

user_1 = Users('John','Doe')
user_1.describe_user()
user_1.greet_user()

admin_1 = Admin('Britan','Hall')
admin_1.describe_admin()
admin_1.privileges.show_privileges()