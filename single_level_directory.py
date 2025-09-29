# Single-Level Directory Simulation in Python

class SingleLevelDirectory:
    def __init__(self):
        self.files = []  # list to store file names

    def create_file(self, file_name):
        if file_name in self.files:
            print(f"File '{file_name}' already exists!")
        else:
            self.files.append(file_name)
            print(f"File '{file_name}' created successfully.")

    def delete_file(self, file_name):
        if file_name in self.files:
            self.files.remove(file_name)
            print(f"File '{file_name}' deleted successfully.")
        else:
            print(f"File '{file_name}' not found!")

    def search_file(self, file_name):
        if file_name in self.files:
            print(f"File '{file_name}' found in directory.")
        else:
            print(f"File '{file_name}' not found in directory.")

    def display_files(self):
        if self.files:
            print("Files in directory:")
            for file in self.files:
                print(f" - {file}")
        else:
            print("Directory is empty.")

if __name__ == "__main__":
    dir_system = SingleLevelDirectory()

    while True:
        print("\n--- Single-Level Directory Menu ---")
        print("1. Create File")
        print("2. Delete File")
        print("3. Search File")
        print("4. Display All Files")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter file name to create: ")
            dir_system.create_file(name)
        elif choice == '2':
            name = input("Enter file name to delete: ")
            dir_system.delete_file(name)
        elif choice == '3':
            name = input("Enter file name to search: ")
            dir_system.search_file(name)
        elif choice == '4':
            dir_system.display_files()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter 1-5.")
