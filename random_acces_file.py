import struct
import os

# Define the employee record structure: ID(int), Name(20 chars), Salary(float)
record_format = 'i20sf'  # i=int, 20s=string of 20 bytes, f=float
record_size = struct.calcsize(record_format)
file_name = "employee.dat"

def write_employee(emp_id, name, salary, position=None):
    name_bytes = name.encode('utf-8')[:20]  # ensure 20 bytes
    name_bytes += b' ' * (20 - len(name_bytes))  # pad with spaces

    with open(file_name, 'r+b') as f:
        if position is not None:
            f.seek(position * record_size)
        else:
            f.seek(0, os.SEEK_END)  # append at end
        f.write(struct.pack(record_format, emp_id, name_bytes, salary))
    print(f"Employee {name} saved successfully.")

def read_employee(position):
    with open(file_name, 'rb') as f:
        f.seek(position * record_size)
        record_data = f.read(record_size)
        if not record_data:
            print("No record found at this position.")
            return
        emp_id, name_bytes, salary = struct.unpack(record_format, record_data)
        name = name_bytes.decode('utf-8').strip()
        print(f"ID: {emp_id}, Name: {name}, Salary: {salary}")

def display_all_employees():
    print("\n--- All Employees ---")
    with open(file_name, 'rb') as f:
        pos = 0
        while True:
            record_data = f.read(record_size)
            if not record_data:
                break
            emp_id, name_bytes, salary = struct.unpack(record_format, record_data)
            name = name_bytes.decode('utf-8').strip()
            print(f"Position {pos}: ID={emp_id}, Name={name}, Salary={salary}")
            pos += 1

# Initialize file if it doesn't exist
if not os.path.exists(file_name):
    open(file_name, 'wb').close()

# Menu-driven program
while True:
    print("\n--- Random Access Employee File ---")
    print("1. Add Employee")
    print("2. Read Employee at Position")
    print("3. Display All Employees")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Employee Salary: "))
        write_employee(emp_id, name, salary)
    elif choice == '2':
        pos = int(input("Enter position of employee to read: "))
        read_employee(pos)
    elif choice == '3':
        display_all_employees()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please enter 1-4.")
