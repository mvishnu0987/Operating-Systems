import threading
import time
import random

# Shared resource
shared_counter = 0

# Mutex lock
mutex = threading.Lock()

# Function for thread to increment counter
def increment_counter(thread_id):
    global shared_counter
    for _ in range(5):
        time.sleep(random.uniform(0.1, 0.5))  # simulate work

        # Acquire mutex before modifying shared resource
        mutex.acquire()
        try:
            local_copy = shared_counter
            print(f"[Thread-{thread_id}] Read counter: {local_copy}")
            local_copy += 1
            shared_counter = local_copy
            print(f"[Thread-{thread_id}] Incremented counter to: {shared_counter}")
        finally:
            # Release mutex
            mutex.release()

if __name__ == "__main__":
    threads = []

    # Create 3 threads
    for i in range(3):
        t = threading.Thread(target=increment_counter, args=(i+1,))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print(f"\n[Main] Final value of shared counter: {shared_counter}")
