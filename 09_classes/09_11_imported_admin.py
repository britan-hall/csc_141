from lib_09_11_imported_admin import *

user_1 = Users('John','Doe')
user_1.describe_user()
user_1.greet_user()

admin_1 = Admin('Britan','Hall')
admin_1.describe_admin()
admin_1.privileges.show_privileges()