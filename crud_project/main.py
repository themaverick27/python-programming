# CRUD project

from pathlib import Path
import os

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))

    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def create_file():
    try:
        readFileAndFolder()
        name = input("please enter file name: ")
        p = Path(name)

        if not p.exists():
            with open(p, 'w') as fs:
                data = input("Add some content in the file: ")
                fs.write(data)
            print("File created successfully!")
        else:
            print("this file already exists!")
    except Exception as err:
        print(f"Error occurred as: {err}")

def read_file():
    try:
        readFileAndFolder()
        name = input("enter the name of the file for reading: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            print("File readed succesfully!")
        else:
            print("file does not exists.")
    except Exception as err:
        print(f"Error occurred as {err}")

def update_file():
    try:
        readFileAndFolder()
        name = input("please enter the file name which you want to update: ")
        p = Path(name)

        if p.exists() and p.is_file():
            print("press 1 for updating name of the file")
            print("press 2 for overwriting the data of the file")
            print("press 3 for appending the data in the file")

            option = int(input("please tell your response: "))
            if option == 1:
                new_name = input("provide the new name of the file: ")
                new_path = Path(new_name)
                p.rename(new_path)

                print("File renamed successfully!")
            elif option == 2:
                with open(p, 'w') as fs:
                    data = input("provide content you want to overwrite in this file: ")
                    fs.write(data)
                print("File overwritten successfully!")
            elif option == 3:
                with open(p, 'a') as fs:
                    data = input("provide content you want to append in this file: ")
                    fs.write(data)
                print("File updated successfully!")
            else:
                print("please enter correct option")
    except Exception as err:
        print(f"Error occurred as {err}")
            
def delete_file():
    try:
        readFileAndFolder()
        name = input("please enter the file name which you want to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("File removed successfully!")
        else:
            print("No such File not exists!")
    except Exception as err:
        print(f"Error occurred as {err}")


print("press 1 to create a file")
print("press 2 to read a file")
print("press 3 to update a file")
print("press 4 to delete a file")

user_input = int(input("please enter your response: "))

if user_input == 1:
    create_file()
elif user_input == 2:
    read_file()
elif user_input == 3:
    update_file()
elif user_input == 4:
    delete_file()