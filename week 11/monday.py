import sqlite3
import csv

with open('pokemon_names_and_descriptions.csv', 'r', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

conn = sqlite3.connect('pokemon.db')

c = conn.cursor()

c.execute('CREATE TABLE pokemon (dex text, english_name text, notes text);')

c.executemany('INSERT INTO pokemon VALUES (?, ?, ?)', data)


c.execute('create table data1999 (year text, pop text);')
c.execute('create table data2000 (year text, pop text);')
c.execute('create table data2001 (year text, pop text);')

conn.commit()