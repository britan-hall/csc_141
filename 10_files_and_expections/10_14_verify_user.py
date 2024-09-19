from pathlib import Path
import json

path = Path('10_files_and_expections/lib_10_14_verify_user.json')

def input_user():
    user = {}
    user_name = input('Enter your name: ')
    user_age = input('Enter your age: ')
    user_location = input('Enter your location: ')

    user['name'] = user_name
    user['age'] = user_age
    user['location'] = user_location

    contents = json.dumps(user)
    path.write_text(contents)
    describe_user(path)

def describe_user(path):
    if path.exists():
        try:
            content = path.read_text()
            user = json.loads(content)
            print(f"Hello {user['name']}!")
            print(f"You are {user['age']} years old and live in {user['location']}.")

            current_user_name = input("Is this you? (yes/no): ").strip().lower()
            if current_user_name == 'no':
                input_user()  
        except json.JSONDecodeError:
            print("Error: The file content is not valid JSON.")
            input_user()
    else:
        input_user()

describe_user(path)
