import csv
import sqlite3

# to read in the data

conn = sqlite3.connect('pokemon.db')

c = conn.cursor()

results = c.execute("select * from pokemon;")

# just get one thing
# first = results.fetchone()

# for i in range(10):
#     print(results.fetchone())

# we get tuples so we can't change things
# new_data = first
# new_data.append('something')
# # print(type(first))

# get all the results

data = results.fetchall()
print("first headers", [tup[0] for tup in results.description])
# print(data)

# trying to get more stuff gets NoneType object
# print(results.fetchone())

dupes = c.execute('select dex, dex || "-" || english_name as new_name from  pokemon;')

print(results.description)

print("dupe headers", [tup[0] for tup in results.description])


headers = [tup[0] for tup in results.description]
names = dupes.fetchall()

with open('pokemonnames.csv', 'w', encoding='utf-8') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(names)

