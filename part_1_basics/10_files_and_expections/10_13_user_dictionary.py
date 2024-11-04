# 3, 2 functions that read and write to a JSON file.

from pathlib import Path
import json

path = Path('10_files_and_expections/lib_10_13_user_dictionary.json')

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
            print(f'Hello {user['name']}!')
            print(f"You are {user['age']} years old and live in {user['location']}.")
        except json.JSONDecodeError:
            print("Error: The file content is not valid JSON.")
    else:
        input_user()

describe_user(path)

    


