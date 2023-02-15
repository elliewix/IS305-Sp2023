import csv

# big verbose way
# with open('pokemon_names_and_descriptions.csv', 'r', encoding = 'utf-8') as infile:
#     csvin = csv.reader(infile)
#     headers = next(csvin)
#     data = [r for r in csvin]
#
# print(headers)
# print(data)

# slightly shorter way

#with open('pokemon_names_and_descriptions.csv', 'r', encoding= 'utf-8') as infile:
#     csvin = csv.reader(infile)
#     headers, *data = csvin
#
# print(headers)
# print(data)

# the super short way

with open('pokemon_names_and_descriptions.csv', 'r', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

# print(headers)
# print(data[:5])


for row in data:
    dex = row[0]
    name = row[1]
    print(dex, name)
    notes = row[2]
