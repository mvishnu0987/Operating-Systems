import threading
import time
import random

# Shared resource
shared_data = 0

# Semaphores
read_count = 0
read_count_lock = threading.Lock()  # Mutex to protect read_count
resource_lock = threading.Semaphore(1)  # Semaphore to protect the shared resource

# Reader function
def reader(reader_id):
    global read_count, shared_data
    for _ in range(5):
        time.sleep(random.uniform(0.1, 1.0))

        # Entry section
        read_count_lock.acquire()
        read_count += 1
        if read_count == 1:
            resource_lock.acquire()  # First reader locks resource
        read_count_lock.release()

        # Critical section (reading)
        print(f"[Reader-{reader_id}] Reading data: {shared_data}")
        time.sleep(random.uniform(0.1, 0.5))  # simulate reading time

        # Exit section
        read_count_lock.acquire()
        read_count -= 1
        if read_count == 0:
            resource_lock.release()  # Last reader releases resource
        read_count_lock.release()

# Writer function
def writer(writer_id):
    global shared_data
    for _ in range(5):
        time.sleep(random.uniform(0.5, 1.5))

        # Entry section
        resource_lock.acquire()  # Writer locks resource

        # Critical section (writing)
        shared_data += 1
        print(f"[Writer-{writer_id}] Writing data: {shared_data}")
        time.sleep(random.uniform(0.2, 0.6))  # simulate writing time

        # Exit section
        resource_lock.release()

if __name__ == "__main__":
    readers = []
    writers = []

    # Create 3 readers
    for i in range(3):
        t = threading.Thread(target=reader, args=(i+1,))
        readers.append(t)

    # Create 2 writers
    for i in range(2):
        t = threading.Thread(target=writer, args=(i+1,))
        writers.append(t)

    # Start all threads
    for t in readers + writers:
        t.start()

    # Wait for all threads to finish
    for t in readers + writers:
        t.join()

    print("\n[Main] Reader-Writer simulation completed.")
