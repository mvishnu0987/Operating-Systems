import os

def grep(pattern, file_name, ignore_case=False, show_line_numbers=False):
    if not os.path.exists(file_name):
        print(f"File '{file_name}' does not exist!")
        return

    with open(file_name, 'r') as f:
        lines = f.readlines()

    print(f"\nSearching for '{pattern}' in file '{file_name}':")
    for idx, line in enumerate(lines, start=1):
        search_line = line.lower() if ignore_case else line
        search_pattern = pattern.lower() if ignore_case else pattern
        if search_pattern in search_line:
            if show_line_numbers:
                print(f"{idx}: {line.strip()}")
            else:
                print(line.strip())

if __name__ == "__main__":
    file_name = input("Enter file name to search: ").strip()
    pattern = input("Enter pattern to search: ").strip()
    ignore_case = input("Ignore case? (y/n): ").strip().lower() == 'y'
    show_line_numbers = input("Show line numbers? (y/n): ").strip().lower() == 'y'

    grep(pattern, file_name, ignore_case, show_line_numbers)
