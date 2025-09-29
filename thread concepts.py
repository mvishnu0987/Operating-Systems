import threading
import time

# Thread function
def thread_task(name):
    print(f"[{name}] Thread started.")
    time.sleep(2)
    print(f"[{name}] Thread finished.")

if __name__ == "__main__":
    # (i) Create threads
    t1 = threading.Thread(target=thread_task, args=("Thread-1",))
    t2 = threading.Thread(target=thread_task, args=("Thread-2",))

    print("Starting threads...\n")
    t1.start()
    t2.start()

    # (ii) Join threads
    print("Joining Thread-1...")
    t1.join()  # Wait until Thread-1 finishes
    print("Thread-1 has finished.\n")

    print("Joining Thread-2...")
    t2.join()  # Wait until Thread-2 finishes
    print("Thread-2 has finished.\n")

    # (iii) Equal: Check if two threads are the same
    t3 = t1
    print(f"t1 == t2? {t1 == t2}")
    print(f"t1 == t3? {t1 == t3}\n")

    # (iv) Exit: Exiting main thread
    print("Main thread exiting.")
