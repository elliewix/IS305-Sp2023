# a = [1, 2, 3]
# b = [500, 600, 700]

# for a_num in a:
#     for b_num in b:
#         print(a_num, b_num)

# a = [1, 2, 3]
# b = [500, 600, 700]
#
# # print(list(range(len(a))))
#
# for i in range(len(a)):
#     top = a[i]
#     bottom = b[i]
#     print(top, bottom)

a = [1, 2, 3, 4]
b = [500, 600, 700]
# b = [500, 600, 700, 800] # will be ignored

# print(list(range(len(a))))

# for i in range(len(a)):
#     top = a[i]
#     bottom = b[i]
#     print(top, bottom)

# how can we protect from this?

# if statements are great here
# but they still let the rest of the code go on
# if len(a) == len(b):
#     for i in range(len(a)):
#         top = a[i]
#         bottom = b[i]
#         print(top, bottom)
# else:
#     print("mismatched lengths")

# length of boths lists must match-
# assert len(a) == len(b), "length bad:" + str(len(a)) + " " + str(len(b))
#
# for i in range(len(a)):
#     top = a[i]
#     bottom = b[i]
#     print(top, bottom)

# an example passing through

a = [1, 2, 3]
b = [500, 600, 700]

assert len(a) == len(b)

for i in range(len(a)):
    top = a[i]
    bottom = b[i]
    print(top, bottom)