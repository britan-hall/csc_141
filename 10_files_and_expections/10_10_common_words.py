from pathlib import Path

path_1 = Path('10_files_and_expections/lib_10_10_common_words_1.txt')
path_2 = Path('10_files_and_expections/lib_10_10_common_words_2.txt')
contents_1 = path_1.read_text()
contents_2 = path_2.read_text()

texts = [contents_1,contents_2]
index = 0

for text in texts:
    index += 1
    print(f'\nText Number {index}')
    the_count = text.count('the')
    print(f"Count of 'the': {the_count}")
    then_count = text.count('there')
    print(f"Count of 'then': {then_count}")
    there_count = text.count('then')
    print(f"Count of 'there': {there_count}")
