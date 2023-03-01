text = """pear
apple
banana
durian
banana
blueberry
apple
banana
strawberry
blueberry
dragonfruit
pear
apple
peach
banana"""

data = text.split("\n")
# print(len(data))

# print(data)

all_chunks = []
temp_chunk = []

# get into groups of three...
for f in data:
    temp_chunk.append(f)
    # len(temp_chunk) # measure if it's full
    if len(temp_chunk) == 3:
        all_chunks.append(temp_chunk) # collect up
        temp_chunk = [] # clear out

if len(temp_chunk) > 0: # check if leftovers
    all_chunks.append(temp_chunk)

# print(all_chunks)


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

all_chunks = []
temp_chunk = []

for i, f in enumerate(data):
    temp_chunk.append(f)
    if f == 'done':
        all_chunks.append(temp_chunk) # collect up
        temp_chunk = [] # clear out
    elif i == len(data) - 1:
        # we've reached the end
        all_chunks.append(temp_chunk)


print(all_chunks)