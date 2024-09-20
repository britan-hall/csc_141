from pathlib import Path

path = Path('10_files_and_expections/lib_10_04_guest.txt')

name = input('What is your name? ')
path.write_text(f'{name}\n')