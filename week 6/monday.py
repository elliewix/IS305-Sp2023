import random
import pathlib

random.seed(50)

words = ['cat', 'snake', 'dog', 'rabbit',
         'sea star', 'slug']
data = {}
for i in range(10):
    formatting_num = str(i).zfill(3)
    word = random.choice(words)
    key = formatting_num + "-" + word
    fake_content = "here's some stuff \n" + (word * i)
    # print(key, fake_content)
    data[key] = fake_content

for key, value in data.items():
    # print(key, value[:10])
    p = pathlib.Path(key + ".txt")
    p.write_text(value)
