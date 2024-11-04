# 1, easy replace function
from pathlib import Path

path = Path('10_files_and_expections/lib_10_01_learning_python.txt')
contents = path.read_text()

print(contents)

contents = contents.replace('Python','C')

print(contents)