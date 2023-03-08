
# is_found = False
# count = 0
# while not is_found:






not_found = True
count = 0
# while not_found:
# while not_found:
#     answer = input("Keep going? y/n")
#     count += 1
#     if answer == "n":
#         not_found = False
        # print("this ran " + str(count) + " times")


count = 0
while count < 10: # juust do for i in range(10)!
    count += 1
    print("still going")

with open('data.txt', 'r', encoding='utf-8') as infile:
    data = [s.strip() for s in infile.readlines()]

# for s in data:
#     print(s, s.isdecimal())

index = 0

while not data[index].isdecimal():
    index += 1

print("first num found on ", index)
print(data[index:])