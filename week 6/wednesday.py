


# def clean_row(row):
#     # do stuff to the row
#     # take care of business
#     return row

import random

numbers_orig = [1, 9, 0, 3, 5, 10]

# new_numbers = numbers_orig[:] # copy an actually new version
# new_numbers.append(13)
# print(numbers_orig)
# print(new_numbers)

# print(numbers_orig is new_numbers)
# print(id(numbers_orig), id(new_numbers))

# print([] is [])
# print('a' is 'a')
# print(1 is 1)
# print(True is True)


data = {}
empty = []

for i in range(10):
    # data[str(i).zfill(3)] = empty # gives copy issue
    data[str(i).zfill(3)] = [i, 'hey'] # the better way

print(data)
data['003'][1] = 'heyyyy    '
# data['003'].append('hey there')

print(data)

def clean_row(row):
    new_row = row.copy()
    # do stuff to it
    text = new_row[1]
    clean_text = text.strip()
    new_row[1] = clean_text

    return new_row

for k, v in data.items():
    print(k, clean_row(v))