import threading
import time
import random

# Number of philosophers
NUM_PHILOSOPHERS = 5

# Create a lock for each fork
forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]

def philosopher(phil_id):
    left_fork = forks[phil_id]
    right_fork = forks[(phil_id + 1) % NUM_PHILOSOPHERS]

    while True:
        # Thinking
        print(f"Philosopher {phil_id} is thinking.")
        time.sleep(random.uniform(1, 3))

        # Hungry: try to pick up forks
        print(f"Philosopher {phil_id} is hungry.")
        # To avoid deadlock, pick up the lower-numbered fork first
        first_fork, second_fork = (left_fork, right_fork) if phil_id % 2 == 0 else (right_fork, left_fork)

        with first_fork:
            print(f"Philosopher {phil_id} picked up first fork.")
            with second_fork:
                print(f"Philosopher {phil_id} picked up second fork and is eating.")
                time.sleep(random.uniform(1, 2))
                print(f"Philosopher {phil_id} has finished eating and puts down forks.")

if __name__ == "__main__":
    # Create threads for philosophers
    philosophers = []
    for i in range(NUM_PHILOSOPHERS):
        t = threading.Thread(target=philosopher, args=(i,))
        philosophers.append(t)
        t.start()

    # Let the simulation run for a while
    time.sleep(20)  # run for 20 seconds
    print("\n[Main] Simulation finished.")
    # Note: In a real simulation, threads would need a way to gracefully exit.
