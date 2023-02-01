import pathlib

myfolder = pathlib.Path('.')

# print(myfolder.absolute())

# allfiles = myfolder.glob('*')
allfiles_recusive = myfolder.rglob('*')
# print(list(allfiles))

python_scripts = [] # anything .py
text_files = [] # anything .txt
for f in allfiles_recusive:
    # print(f, f.is_dir())
    # if not f.is_dir():
    #     print(f)
    if f.is_dir() == False:
        # print(f, f.suffix)
        if f.suffix == '.txt':
            text_files.append(f)
        elif f.suffix == '.py':
            python_scripts.append(f)
# print(text_files)
# print(python_scripts)

for f in text_files:
    # print(f)
    f.unlink()

