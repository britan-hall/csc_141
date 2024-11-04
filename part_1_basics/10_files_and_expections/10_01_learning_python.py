# 1, pretty simple to understand about setting Paths

from pathlib import Path

path = Path('10_files_and_expections/lib_10_01_learning_python.txt')

contents = path.read_text()
print(contents)

string = ''
lines = contents.splitlines()
for line in lines:
    string += f' {line}'
print(string)
