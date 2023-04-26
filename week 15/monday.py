import csv

with open('cleaned_pokemon_info-1.csv', 'r', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

# print(data)

import string
import random
from collections import Counter


# bare bones
# word = ""
#
# for _ in range(5):
#     word += random.choice(string.ascii_lowercase)
# print(string.ascii_lowercase)
# print(word)

# p_names = []
# for row in data:
#     name = row[0]
#     p_names.append(name)
#
# print(p_names)

p_names = [r[0].lower() for r in data]

# letters = [list(name) for name in p_names]
# letters = []
# for name in p_names:
#     letters += list(name)

letters = []
[letters.extend(list(name)) for name in p_names]

# print(letters)

newname = ""
for _ in range(10):
    newname += random.choice(letters)

# print(newname)

####

counted_letters = Counter(letters)
num_letters = len(letters)

# print(counted_letters)

# letter_ratios = {}
#
# for letter, count in counted_letters.items():
#     letter_ratios[letter] = round(count / num_letters, 4)

letter_ratios = {letter: {'count': count, 'ratio': round(count/num_letters, 4)} for letter, count in counted_letters.items()}

print(letter_ratios)

unique_letters = []
ratios = []

print([(unique_letters.append(letter), ratios.append(data['ratio'])) for letter, data in letter_ratios.items()])

print(unique_letters)
print(ratios)


