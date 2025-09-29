import os
import stat

def file_seek_example(file_name):
    with open(file_name, 'w+') as f:
        f.write("Hello UNIX I/O System Calls\n")
        f.seek(0)  # Move pointer to start
        content = f.read()
        print(f"\nFile content after seek to start:\n{content}")

def file_stat_example(file_name):
    info = os.stat(file_name)
    print(f"\n--- File Stats for '{file_name}' ---")
    print(f"Size: {info.st_size} bytes")
    print(f"Permissions: {oct(info.st_mode)}")
    print(f"Last modified: {info.st_mtime}")
    print(f"Last accessed: {info.st_atime}")

def directory_example(dir_name):
    print(f"\nListing files in directory '{dir_name}':")
    with os.scandir(dir_name) as entries:
        for entry in entries:
            if entry.is_file():
                print(f"File: {entry.name}")
            elif entry.is_dir():
                print(f"Directory: {entry.name}")

if __name__ == "__main__":
    file_name = "testfile.txt"
    dir_name = "."

    # Demonstrate seek
    file_seek_example(file_name)

    # Demonstrate stat
    file_stat_example(file_name)

    # Demonstrate opendir / readdir
    directory_example(dir_name)
