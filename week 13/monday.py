name = "mr mime"
num = 2
# grams = []

def grams(num, name):
    ngrams = []
    for i in range(len(name)):
        if i + num > len(name):
            break
        pair = name[i:i + num]
        ngrams.append(pair)
    return ngrams
    # print(i, i + num, pair)
    # if not " " in pair:
    #     grams.append(pair)

print(grams(2, "mr") + grams(2, "mime"))
