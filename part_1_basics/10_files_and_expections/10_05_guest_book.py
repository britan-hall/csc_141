from pathlib import Path

path = Path('10_files_and_expections/lib_10_05_guest_book.txt')
add_name_active = True
guest_names = []

def add_name(add_name_active):
    while add_name_active:
        print('Enter "quit" to exit the program and write to book')
        user_input = input(f'Guest name: ')
        if user_input.lower() == "quit":
            add_name_active = False
        else:
            guest_names.append(user_input)

    if guest_names:
        guest_string = ''
        for name in guest_names:
            guest_string += f'{name}\n'
        path.write_text(guest_string)

add_name(add_name_active)
