from pathlib import Path
import json

number = int(input('What is your favorite number? '))

path = Path('10_files_and_expections/lib_10_11_favorite_number.json')
contents = json.dumps(number)
path.write_text(contents)