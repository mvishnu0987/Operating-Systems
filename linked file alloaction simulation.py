class LinkedFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.directory = {"first": None, "last": None}  # Pointers to first and last blocks
        self.blocks = {}  # Dictionary to store blocks and pointers

    def add_block(self, data):
        # Create a new block number
        block_number = len(self.blocks) + 1
        # New block points to None initially
        self.blocks[block_number] = {"data": data, "next": None}

        if self.directory["first"] is None:
            # First block of the file
            self.directory["first"] = block_number
            self.directory["last"] = block_number
        else:
            # Link the previous last block to the new block
            last_block = self.directory["last"]
            self.blocks[last_block]["next"] = block_number
            self.directory["last"] = block_number

        print(f"Block {block_number} added with data: '{data}'")

    def read_file(self):
        print(f"\n--- Reading file '{self.file_name}' ---")
        current = self.directory["first"]
        if current is None:
            print("File is empty!")
            return
        while current is not None:
            block = self.blocks[current]
            print(f"Block {current}: {block['data']}")
            current = block["next"]

    def display_directory(self):
        print(f"\nDirectory of '{self.file_name}': First Block = {self.directory['first']}, Last Block = {self.directory['last']}")

if __name__ == "__main__":
    file = LinkedFile("MyLinkedFile")

    while True:
        print("\n--- Linked File Allocation ---")
        print("1. Add Block")
        print("2. Read File")
        print("3. Display Directory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter data for new block: ")
            file.add_block(data)
        elif choice == '2':
            file.read_file()
        elif choice == '3':
            file.display_directory()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter 1-4.")
