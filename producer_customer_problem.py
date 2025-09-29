import threading
import time
import random

# Shared buffer
buffer = []
buffer_size = 5

# Semaphores
empty = threading.Semaphore(buffer_size)  # Initially, buffer has 'buffer_size' empty slots
full = threading.Semaphore(0)             # Initially, buffer has 0 full slots
mutex = threading.Lock()                  # For mutual exclusion

# Producer function
def producer():
    global buffer
    for i in range(10):  # produce 10 items
        item = random.randint(1, 100)
        empty.acquire()  # wait if buffer is full
        mutex.acquire()  # enter critical section
        buffer.append(item)
        print(f"[Producer] Produced: {item} | Buffer: {buffer}")
        mutex.release()  # exit critical section
        full.release()   # signal that buffer has an item
        time.sleep(random.uniform(0.5, 1.5))  # simulate production time

# Consumer function
def consumer():
    global buffer
    for i in range(10):  # consume 10 items
        full.acquire()    # wait if buffer is empty
        mutex.acquire()   # enter critical section
        item = buffer.pop(0)
        print(f"[Consumer] Consumed: {item} | Buffer: {buffer}")
        mutex.release()   # exit critical section
        empty.release()   # signal that buffer has empty slot
        time.sleep(random.uniform(1, 2))  # simulate consumption time

if __name__ == "__main__":
    # Create producer and consumer threads
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to complete
    t1.join()
    t2.join()

    print("\n[Main] Producer-Consumer simulation completed.")
