# import pathlib
#
# p = pathlib.Path('data')
#
# p.mkdir(exist_ok=True)
#
# print(p.exists())
# print(p.is_dir())
#

import pathlib

datafolder = pathlib.Path('data')
files = datafolder.glob('*')

all_files = []
all_folders = []

for f in files:
    if f.is_dir():
        # print("a folder:", f)
        all_folders.append(f)
    else:
        # print("a file:", f)
        all_files.append(f)

print("the files:", all_files)
print("the folders", all_folders)


text = "this is a sentence"
p = pathlib.Path('data/document.txt')
p.write_text(text)