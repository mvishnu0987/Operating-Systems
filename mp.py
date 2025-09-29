import os
import subprocess

def main():
    print("\n--- Parent Process ---")
    print("Parent PID:", os.getpid())
    print("Parent's Parent PID:", os.getppid())

    # Launch a child process (this script itself with --child argument)
    subprocess.run(["python", __file__, "--child"])

if __name__ == "__main__":
    import sys
    if "--child" in sys.argv:
        # Child process code
        print("\n--- Child Process ---")
        print("Child PID:", os.getpid())
        print("Parent PID:", os.getppid())
    else:
        main()
