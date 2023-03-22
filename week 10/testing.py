import csv

with open('pokemon_names_and_descriptions.csv', 'r', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

# let's add some columns!
# okay yes some of this stuff you can do in pandas, but you may not always have the choice

# first, to get around a bit of the issue with just using position numbers
# we can use the index method to grab the positions of these columns

print(headers)

i_dex = headers.index('National Pokédex\nnumber')
i_name = headers.index('English')
i_notes = headers.index('Notes')

new_rows = []
all_notes = " ".join([r[2] for r in data]).lower()

# we can grab the columns based on these things now 
for row in data:
    dex = row[i_dex]
    name = row[i_name]
    notes = row[i_notes]

    notes_len = len(notes)
    has_name = notes_len != 0
    name_count = all_notes.count(name.lower())
    name_used = name_count != 0
    new_row = [dex, name, notes, notes_len, has_name, name_count, name_used]
    new_rows.append(new_row)
    print(new_row)

# are there any of these that are false, though, to being mentioned by another pokeme
# how can we omit itself? maybe many ways


for i, row in enumerate(data):
    other_notes = " ".join([r[2] for j, r in enumerate(data) if i != j]).lower()
    dex = row[i_dex]
    name = row[i_name]
    notes = row[i_notes]

    notes_len = len(notes)
    has_name = notes_len != 0
    name_count = other_notes.count(name.lower())
    name_used = name_count != 0
    new_row = [dex, name, notes, notes_len, has_name, name_count, name_used]
    new_rows.append(new_row)
    print(new_row)