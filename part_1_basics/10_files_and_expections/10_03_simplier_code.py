# 1, simple way to format the text in the path file
from pathlib import Path

path = Path('10_files_and_expections/lib_10_01_learning_python.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)
