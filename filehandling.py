# file=open('simple.txt','w')
# file.write("Accept what you are and enjoy your life.")
# file=open("simple.txt",'r')
# content=file.read()
# file.close
# print(f"content of 'simple.txt':{content}")
import os
def create_file(filename):
    try:
        with open (filename,'x') as f:
            print(f"File Name {filename}: Created Successfully!")
    except FileExistsError:
        print(f"File Name {filename}: file already exist!")
    except Exception as E:
        print(f"FileName {filename}: Error Occured!")
def view_all_file():
    files=os.listdir()
    if not files:
        print('No files found.')
    else:
        print('Files found')
        for file in files:
            print(file)
def delete_files(filename):
    try:
        os.remove(filename)
        print(f"File already removed:{filename}")
    except FileNotFoundError:
        print("File Not Found")
    except Exception as E:
        print("Already Error Occured")
def read_files(filename):
    try:
        with open('simple.txt','r') as f:
            content=f.read()
        print(f"Content of '{filename}':/n{content}")
    except FileNotFoundError:
        print("File Not Found")
    except Exception as E:
        print("An Error Occured")
def edit_files(filename):
    try:
        with open('simple.txt') as f:
            content = input('Enter any any filename =')
            f.write(content)
        print(f"Added new file successfully:{filename}")
    except FileNotFoundError:
        print("File Not found")
    except Exception:
        print("An Error Occured")
def main():
    while True:
        print("File Mangement App")
        print("1:create file")
        print("2:View all file")
        print("3:Delete file")
        print("4:Read file")
        print("5:Edit file")
        print("6:Exit")

        choice=input("Enter your choice(1-6)=")
        if choice=='1':
            filename=input("Enter a file name to create file=")
            create_file(filename)
        elif choice=='2':
            view_all_file()
        elif choice=='3':
            filename=input("Enter a file name to delete file=")
            delete_files(filename)
        elif choice=='4':
            filename=input("Enter a file name to read file=")
            read_files(filename)
        elif choice=='5':
            filename=input("Enter a file name to edit file=")
            edit_files(filename)
        elif choice=='6':
            print("Closing the app. Hope you feel happy.....")
            break
        else:
            print("Invalid Syntax...")
if __name__ == "__main__":
    main()
            