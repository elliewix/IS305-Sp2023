import random
import pathlib

fakedata = []

pets = ['snake', 'cat', 'dog', 'spider']
words = ["cute", "fuzzy", "present", "lovable", "stubborn"]

for i in range(1000):
    pet = random.choice(pets)
    stu_id = random.randint(600000, 699999) # "unique" enough id
    phrase = "my " + pet + " is " + random.choice(words)
    # filename should be id + pet
    targetfolder = pathlib.Path('data')
    # print(targetfolder.is_dir())
    fname = pathlib.Path(str(i).zfill(3) + "-" + pet + ".txt")
    # print(fname)
    out = targetfolder / fname

    # contents should be the phrase
    out.write_text(phrase)
