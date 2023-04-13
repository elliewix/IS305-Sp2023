import string

def ngram_letters(name, num):
    name = name.lower()
    nameparts = [n.strip(string.punctuation) for n in name.split()]
    # print(nameparts)
    grams = []
    if len(nameparts) > 1:
        for part in nameparts:
            grams += ngram_letters(part,num)
    else:
        for i in range(len(name)):
            if i + num > len(name):
                break
            grams.append(name[i:i + num])
    # print("grams", grams)
    return grams

if __name__ == '__main__':
    critters = ["Pikachu", "Mr. Mime", "Mega Charizard", "Farfetch'd"]

    parts = []

    for name in critters:
        parts += ngram_letters(name, 2)

    print(parts)
