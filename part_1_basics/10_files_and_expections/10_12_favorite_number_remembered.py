# 2, easy combination from the last two programs

from pathlib import Path
import json

path = Path('10_files_and_expections/lib_10_11_favorite_number.json')

def favorite_number(path):
    if path.exists():
        try:
            content = path.read_text()
            number = json.loads(content)
            print(f'I know your favorite number is {number}!')
        except json.JSONDecodeError:
            print("Error: The file content is not valid JSON.")

    else:
        try:
            number = int(input('What is your favorite number? '))
            contents = json.dumps(number)
            path.write_text(contents)
            print("Your favorite number has been saved!")
        except ValueError:
            print("Please enter a valid integer.")

favorite_number(path)
