class SequentialFile:
    def __init__(self):
        self.records = []  # List to store file records

    def add_record(self, record):
        self.records.append(record)
        print(f"Record '{record}' added to file.")

    def display_file(self):
        print("\n--- File Records ---")
        for idx, record in enumerate(self.records):
            print(f"Record {idx + 1}: {record}")

    def read_record(self, record_number):
        if record_number <= 0 or record_number > len(self.records):
            print("Invalid record number!")
            return
        print(f"\nAccessing Record {record_number} sequentially:")
        for i in range(record_number):
            print(f"Record {i + 1}: {self.records[i]}")

if __name__ == "__main__":
    file = SequentialFile()

    while True:
        print("\n--- Sequential File Allocation ---")
        print("1. Add Record")
        print("2. Display All Records")
        print("3. Read a Record")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            record = input("Enter record to add: ")
            file.add_record(record)
        elif choice == '2':
            file.display_file()
        elif choice == '3':
            rec_num = int(input("Enter record number to read: "))
            file.read_record(rec_num)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter 1-4.")
