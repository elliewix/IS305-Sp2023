import csv

with open('pokemon_names_and_descriptions.csv', 'r', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)


# for row in data:
#     dex = row[0]
#     notes = row[2]
#     # print(dex, notes)
#     if notes == '':
#         # print("before", [dex, notes])
#         # notes = "Missing" # notes isn't connected to the data
#         print("after", [dex, notes])

for row in data:
    notes = row[2]
    if notes == '':
        # print(notes)
        row[2] = "Missing" # now we're mutating the actual data
    # print(row)

for row in data:
    print(row)
# with open('smaller_pokemon.csv', 'w', encoding='utf-8', newline="") as outfile:
#     csvout = csv.writer(outfile)
#     csvout.writerow(headers)
#     csvout.writerows(data_small)


