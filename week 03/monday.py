import pathlib

for i in range(30):
    num = str(i)
    text = "here's some stuff " + num
    filepath = "text" + num + ".txt"
    p = pathlib.Path(filepath)

    # print(p.exists()) # return t/f
    if not p.exists():
        p.write_text(text)
    else:
        print("already done " + str(p))

targetdir = pathlib.Path('datafiles')
# stuff

targetdir.mkdir(exist_ok=True)

print(targetdir.exists())
