a = [1, 2, 3, 4]
b = [500, 600, 700, 800]

assert len(a) == len(b), "lengths need to match"

pairs = list(zip(b, a))

# for p in pairs:
#     b_val, a_val = p
#     print(b_val, a_val)

# for key, value in dict.items().....
for b_val, a_val in pairs:
    print(b_val, a_val)


a = [1, 2, 3, 4]
b = [500, 600, 700, 800]
c = ['a', 'b', 'c', 'd']
d = ['w', 'x', 'y', 'z']

# only need list here to see the values
# print(list(zip(a, b, c, d)))

# they will unpack as normal from the generator
for t in zip(a, b, c, d):
    key, *row = t
    print(key, row)
    # key, *row, end = t
    # print(key, row, end)

# database = {key: row for []}
# data = [[key, row] for key, *row in zip(a, b, c, d)]
# print(data)
database = {key: row for key, *row in zip(a, b, c, d)}
print(database)

database2 = {}
for key, *row in zip(a, b, c, d):
    database2[key] = row

print(database2)