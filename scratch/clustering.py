text = """pear
apple
banana
durian
done
banana
blueberry
apple
banana
done
strawberry
done
blueberry
dragonfruit
pear
apple
done
peach
banana"""

data = text.split("\n")
print(data)

all_chucks = []
temp_chunk = []

for index, item in enumerate(data):
    if item == "done":
        all_chucks.append(temp_chunk)
        temp_chunk = []
    elif (index + 1) == len(data):
        temp_chunk.append(item)
        all_chucks.append(temp_chunk)
    else:
        temp_chunk.append(item)

print(all_chucks)
