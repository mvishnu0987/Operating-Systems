import threading
import time
import random

# Shared resource
buffer = []
buffer_size = 5

# Semaphores
empty = threading.Semaphore(buffer_size)  # Counts empty slots
full = threading.Semaphore(0)             # Counts full slots
mutex = threading.Lock()                  # Mutex for buffer access

# Producer function
def producer():
    global buffer
    for i in range(10):
        item = random.randint(1, 100)
        empty.acquire()  # Wait for empty slot
        mutex.acquire()  # Enter critical section

        buffer.append(item)
        print(f"[Producer] Produced item: {item} | Buffer: {buffer}")

        mutex.release()  # Exit critical section
        full.release()   # Signal that a new item is available
        time.sleep(random.uniform(0.1, 0.5))

# Consumer function
def consumer():
    global buffer
    for i in range(10):
        full.acquire()   # Wait for item to be available
        mutex.acquire()  # Enter critical section

        item = buffer.pop(0)
        print(f"[Consumer] Consumed item: {item} | Buffer: {buffer}")

        mutex.release()  # Exit critical section
        empty.release()  # Signal that a slot is free
        time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    # Create producer and consumer threads
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()

    print("\n[Main] Producer-Consumer simulation completed.")
