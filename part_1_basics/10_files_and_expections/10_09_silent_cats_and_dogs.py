from pathlib import Path

path_1 = Path('10_files_and_expections/lib_10_08_cats_and_dogs_1.txt')
path_2 = Path('10_files_and_expections/lib_10_08_cats_and_dogs_2.txt')

def show_names():
    while True:
        try:
            content_1 = path_1.read_text()
            print(content_1)
            break
        except FileNotFoundError:
            pass
            break
    
    while True:
        try:
            content_2 = path_2.read_text()
            print(content_2)
            break
        except FileNotFoundError:
            pass     
            break

show_names()
    