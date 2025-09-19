# file handling
from pathlib import Path

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items} ")


def createFile():
    try:
        readFileAndFolder()
        name = input("please tell your file name - ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What your want to write in this file - ")
                fs.write(data)
            print("File created successfully")
        else:
            print("this file already exist")
    except Exception as err:
        print(f"An error occured is {err}")