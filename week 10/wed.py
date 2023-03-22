import csv

with open('pokemon_names_and_descriptions.csv', 'r', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

i_dex = headers.index("National Pokédex\nnumber")
i_name = headers.index("English")
i_notes = headers.index("Notes")

# print(i_dex, i_name, i_notes)

# all_notes = ""
# for row in data:
#     all_notes += row[i_notes] + '\n'

# all_notes = "\n".join([r[i_notes] for r in data])

# print(all_notes.lower().count('pikachu'))

all_new_rows = []

for i, row in enumerate(data):
    dex = row[i_dex]
    name = row[i_name]
    notes = row[i_notes]

    # all_notes_but_this_one = ""
    # for j, j_row in enumerate(data):
    #     if j != i:
    #         all_notes_but_this_one += j_row[i_notes].lower()
    # print(name, all_notes_but_this_one.count(name.lower()))
    #
    all_notes_but_this_one = " ".join([j_row[i_notes].lower() for j, j_row in enumerate(data) if i != j])
    name_count = all_notes_but_this_one.count(name.lower())


    notes_length = len(notes)
    notes_empty = notes_length == 0
    med_notes = notes_length > 500
    # do we want to add a boundary?
    long_notes = notes_length > 1000

    new_row = [dex, name, notes_length, med_notes, name_count]
    all_new_rows.append(new_row)

with open('new_pokemondata.csv', 'w', encoding='utf-8') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(['dex', 'name', 'notes_length', 'med_notes', 'name_count'])
    csvout.writerows(all_new_rows)