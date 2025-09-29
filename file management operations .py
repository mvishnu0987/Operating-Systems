import os

def create_file(file_name):
    with open(file_name, 'w') as f:
        print(f"File '{file_name}' created successfully.")

def write_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)
        print(f"Data written to '{file_name}' successfully.")

def append_file(file_name, data):
    with open(file_name, 'a') as f:
        f.write(data)
        print(f"Data appended to '{file_name}' successfully.")

def read_file(file_name):
    if not os.path.exists(file_name):
        print(f"File '{file_name}' does not exist!")
        return
    with open(file_name, 'r') as f:
        content = f.read()
        print(f"\n--- Content of '{file_name}' ---\n{content}")

def rename_file(old_name, new_name):
    if not os.path.exists(old_name):
        print(f"File '{old_name}' does not exist!")
        return
    os.rename(old_name, new_name)
    print(f"File renamed from '{old_name}' to '{new_name}'.")

def delete_file(file_name):
    if not os.path.exists(file_name):
        print(f"File '{file_name}' does not exist!")
        return
    os.remove(file_name)
    print(f"File '{file_name}' deleted successfully.")

if __name__ == "__main__":
    while True:
        print("\n--- File Management System ---")
        print("1. Create File")
        print("2. Write File")
        print("3. Append File")
        print("4. Read File")
        print("5. Rename File")
        print("6. Delete File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            fname = input("Enter file name to create: ")
            create_file(fname)
        elif choice == '2':
            fname = input("Enter file name to write: ")
            data = input("Enter data to write: ")
            write_file(fname, data)
        elif choice == '3':
            fname = input("Enter file name to append: ")
            data = input("Enter data to append: ")
            append_file(fname, data)
        elif choice == '4':
            fname = input("Enter file name to read: ")
            read_file(fname)
        elif choice == '5':
            old_name = input("Enter current file name: ")
            new_name = input("Enter new file name: ")
            rename_file(old_name, new_name)
        elif choice == '6':
            fname = input("Enter file name to delete: ")
            delete_file(fname)
        elif choice == '7':
            print("Exiting File Management System...")
            break
        else:
            print("Invalid choice! Please enter 1-7.")
