class IndexedFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.index_block = []  # Index block stores pointers to data blocks
        self.data_blocks = {}  # Dictionary simulates actual blocks

    def add_block(self, data):
        block_number = len(self.data_blocks) + 1
        self.data_blocks[block_number] = data
        self.index_block.append(block_number)  # Update index block
        print(f"Block {block_number} added with data: '{data}'")

    def display_index_block(self):
        print(f"\nIndex Block for '{self.file_name}': {self.index_block}")

    def read_block(self, block_number):
        if block_number not in self.data_blocks:
            print(f"Block {block_number} does not exist!")
        else:
            print(f"Reading Block {block_number}: {self.data_blocks[block_number]}")

    def display_file(self):
        print(f"\n--- File: {self.file_name} ---")
        for idx, block_num in enumerate(self.index_block, start=1):
            print(f"Block {idx} -> Data: {self.data_blocks[block_num]}")

if __name__ == "__main__":
    file = IndexedFile("MyFile")

    while True:
        print("\n--- Indexed File Allocation ---")
        print("1. Add Data Block")
        print("2. Display Index Block")
        print("3. Read a Block")
        print("4. Display Entire File")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter data for new block: ")
            file.add_block(data)
        elif choice == '2':
            file.display_index_block()
        elif choice == '3':
            block_number = int(input("Enter block number to read: "))
            file.read_block(block_number)
        elif choice == '4':
            file.display_file()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter 1-5.")
