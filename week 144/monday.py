from lab5code import ngram_letters
from collections import Counter

names = ["pikachu", 'kazam', 'kazzaa', "azurill", "bedrill", "azuazurilril"]

allduos = []
pokemon_counts = []
for n in names:
    duos = ngram_letters(n, 2)
    allduos += duos
    counted = dict(Counter(duos))
    counted['name'] = n
    counted['type'] = 'pokemon'
    pokemon_counts.append(counted)

headers = list(set(allduos))
headers.insert(0, 'name')
headers.append('type')
print(headers)
print(pokemon_counts)

for data in pokemon_counts:
    print(data)
    name = data['name']
    type = data['type']
    row = [0] * len(headers)
    name_i = headers.index('name')
    type_i = headers.index('type')
    row[name_i] = name
    row[type_i] = type
    for label in headers:
        if label in data:
            print(label, data[label], headers.index(label))

