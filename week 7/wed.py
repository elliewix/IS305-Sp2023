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
#
# for i, f in enumerate(data):
#     temp_chunk.append(f)
#     if f == 'done':
#         # temp_chunk.pop(-1) # an option to remove the last thing
#         all_chunks.append(temp_chunk) # collect up
#         temp_chunk = [] # clear out
#     elif i == len(data) - 1:
#         # we've reached the end
#         all_chunks.append(temp_chunk)

stops = ['done', 'finished', 'end']
for i, f in enumerate(data):
    # temp_chunk.append(f)
    if f in stops: # if we had a list
    # if f == 'done': # if f in stops:
        # don't need to add anything to temp
        # temp_chunk.pop(-1) # an option to remove the last thing
        all_chunks.append(temp_chunk) # collect up
        temp_chunk = [] # clear out
    elif i == len(data) - 1:
        # do we need to add something to temp?
        temp_chunk.append(f)
        # we've reached the end
        all_chunks.append(temp_chunk)
    else:
        temp_chunk.append(f)


# print(all_chunks)



nums = [352, 353, 354, 416, 417, 419, 420, 487, 488, 489, 490, 491, 505, 569, 663, 736, 740, 741, 753, 754, 810, 811, 812, 872, 873, 874, 963, 965, 969, 976, 977]



