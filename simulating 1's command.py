import os
import stat
import time

def ls(directory="."):
    print(f"Listing files in directory: {directory}\n")
    
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                file_type = "File" if entry.is_file() else "Directory" if entry.is_dir() else "Other"
                size = entry.stat().st_size
                permissions = stat.filemode(entry.stat().st_mode)
                last_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(entry.stat().st_mtime))
                
                print(f"{file_type:10} {permissions} {size:8} bytes  {last_modified}  {entry.name}")
    except FileNotFoundError:
        print(f"Directory '{directory}' not found!")

if __name__ == "__main__":
    dir_name = input("Enter directory to list (press Enter for current directory): ").strip()
    if dir_name == "":
        dir_name = "."
    ls(dir_name)
