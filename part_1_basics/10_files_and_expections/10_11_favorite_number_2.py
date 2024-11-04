# 1, simple way to read data from a JSON file

from pathlib import Path
import json

path = Path('10_files_and_expections/lib_10_11_favorite_number.json')
content = path.read_text()
number = json.loads(content)

print(f'I know your favorite number is {number}!')
