import threading
import time

# Function for thread 1
def print_numbers():
    for i in range(1, 6):
        print(f"[Thread-1] Number: {i}")
        time.sleep(1)  # simulate work

# Function for thread 2
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"[Thread-2] Letter: {letter}")
        time.sleep(1.5)  # simulate work

if __name__ == "__main__":
    # Create threads
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)

    # Start threads
    t1.start()
    t2.start()

    # Wait for both threads to finish
    t1.join()
    t2.join()

    print("\n[Main] Multithreading demo completed.")
