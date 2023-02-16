import random
import csv

fakedata = []

pets = ['snake', 'cat', 'dog', 'spider']
words = ["cute", "fuzzy", "present", "lovable", "stubborn"]

for _ in range(100):
    num = random.randint(1, 10)
    pet = random.choice(pets)
    stu_id = random.randint(600000, 699999) # "unique" enough id
    phrase = "they are " + random.choice(words)
    row = [stu_id, num, pet, phrase]
    # print(row)
    fakedata.append(row)

headers = ['stu_id', 'num', 'pet', 'phrase']

with open('petdata.csv', 'w', encoding='utf-8', newline='') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(fakedata)

