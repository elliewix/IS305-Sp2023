# bigrams = ['pi', 'ik', 'ka', 'az', 'zu', 'ur',
#            're', 'ka', 're',  'ka', 'az', 'zu']
#
# print(bigrams)
# print(list(set(bigrams)))

from lab5code import ngram_letters

names = ["pikachu", 'kazam', 'kazzaa', "azurill", "bedrill"]

grams = []
for name in names:
    # grams.append(ngram_letters(name, 2))
    grams += ngram_letters(name, 2) # keep it flat

headers = list(set(grams))

row = []

# for i in range(len(headers)): # sure but long
#     row.append(0)
#

#
# row = ['pikachu'] + [0] * len(headers) + ['pokemon']
#
# print(row)

# pretend these are all pokemon

all_pokemon = []
for name in names:
    row = [name] + [0] * len(headers) + ['pokemon']
    all_pokemon.append(row)

headers.insert(0, 'name')
headers.append('class')
print(headers)
print(all_pokemon[0])


print(headers.index('ll'))

all_pokemon[1][2] = 5

for p in all_pokemon:
    print(p)
    # print(p[headers.index('ll')])