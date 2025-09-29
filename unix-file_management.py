import os

def create_file(file_name):
    fd = os.open(file_name, os.O_CREAT | os.O_WRONLY)
    os.close(fd)
    print(f"File '{file_name}' created successfully.")

def write_file(file_name, data):
    fd = os.open(file_name, os.O_WRONLY)
    os.write(fd, data.encode())
    os.close(fd)
    print(f"Data written to '{file_name}' successfully.")

def read_file(file_name):
    fd = os.open(file_name, os.O_RDONLY)
    content = os.read(fd, 1024)  # Read up to 1024 bytes
    os.close(fd)
    print(f"Content of '{file_name}':")
    print(content.decode())

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
    print(f"File renamed from '{old_name}' to '{new_name}'.")

def delete_file(file_name):
    os.unlink(file_name)
    print(f"File '{file_name}' deleted successfully.")

if __name__ == "__main__":
    while True:
        print("\n--- UNIX File Management Simulation ---")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Rename File")
        print("5. Delete File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            fname = input("Enter file name to create: ")
            create_file(fname)
        elif choice == '2':
            fname = input("Enter file name to write: ")
            data = input("Enter data to write: ")
            write_file(fname, data)
        elif choice == '3':
            fname = input("Enter file name to read: ")
            read_file(fname)
        elif choice == '4':
            old_name = input("Enter current file name: ")
            new_name = input("Enter new file name: ")
            rename_file(old_name, new_name)
        elif choice == '5':
            fname = input("Enter file name to delete: ")
            delete_file(fname)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter 1-6.")
