# Two-Level Directory Simulation in Python

class TwoLevelDirectory:
    def __init__(self):
        self.main_directory = {}  # Each key is a folder/user, value is a list of files

    def create_folder(self, folder_name):
        if folder_name in self.main_directory:
            print(f"Folder '{folder_name}' already exists!")
        else:
            self.main_directory[folder_name] = []
            print(f"Folder '{folder_name}' created successfully.")

    def create_file(self, folder_name, file_name):
        if folder_name not in self.main_directory:
            print(f"Folder '{folder_name}' does not exist!")
            return
        if file_name in self.main_directory[folder_name]:
            print(f"File '{file_name}' already exists in folder '{folder_name}'!")
        else:
            self.main_directory[folder_name].append(file_name)
            print(f"File '{file_name}' created successfully in folder '{folder_name}'.")

    def delete_file(self, folder_name, file_name):
        if folder_name in self.main_directory and file_name in self.main_directory[folder_name]:
            self.main_directory[folder_name].remove(file_name)
            print(f"File '{file_name}' deleted from folder '{folder_name}'.")
        else:
            print(f"File '{file_name}' not found in folder '{folder_name}'.")

    def search_file(self, folder_name, file_name):
        if folder_name in self.main_directory and file_name in self.main_directory[folder_name]:
            print(f"File '{file_name}' found in folder '{folder_name}'.")
        else:
            print(f"File '{file_name}' not found in folder '{folder_name}'.")

    def display_files(self, folder_name=None):
        if folder_name:
            if folder_name in self.main_directory:
                print(f"Files in folder '{folder_name}': {self.main_directory[folder_name]}")
            else:
                print(f"Folder '{folder_name}' does not exist!")
        else:
            print("All folders and files:")
            for folder, files in self.main_directory.items():
                print(f"Folder '{folder}': {files}")

if __name__ == "__main__":
    dir_system = TwoLevelDirectory()

    while True:
        print("\n--- Two-Level Directory Menu ---")
        print("1. Create Folder")
        print("2. Create File")
        print("3. Delete File")
        print("4. Search File")
        print("5. Display Files in Folder")
        print("6. Display All Folders and Files")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            folder = input("Enter folder name to create: ")
            dir_system.create_folder(folder)
        elif choice == '2':
            folder = input("Enter folder name: ")
            file_name = input("Enter file name to create: ")
            dir_system.create_file(folder, file_name)
        elif choice == '3':
            folder = input("Enter folder name: ")
            file_name = input("Enter file name to delete: ")
            dir_system.delete_file(folder, file_name)
        elif choice == '4':
            folder = input("Enter folder name: ")
            file_name = input("Enter file name to search: ")
            dir_system.search_file(folder, file_name)
        elif choice == '5':
            folder = input("Enter folder name to display files: ")
            dir_system.display_files(folder)
        elif choice == '6':
            dir_system.display_files()
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter 1-7.")
