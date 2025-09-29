# Banker's Algorithm Simulation in Python

def is_safe_state(available, max_demand, allocation):
    num_processes = len(max_demand)
    num_resources = len(available)

    # Calculate Need matrix
    need = [[max_demand[i][j] - allocation[i][j] for j in range(num_resources)]
            for i in range(num_processes)]

    finish = [False] * num_processes
    safe_sequence = []
    work = available.copy()

    while len(safe_sequence) < num_processes:
        allocated_in_this_round = False
        for i in range(num_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):
                for j in range(num_resources):
                    work[j] += allocation[i][j]
                safe_sequence.append(i)
                finish[i] = True
                allocated_in_this_round = True
        if not allocated_in_this_round:
            break  # No allocation possible, unsafe state

    if len(safe_sequence) == num_processes:
        print("System is in a SAFE state.")
        print("Safe sequence:", ' -> '.join([f"P{p}" for p in safe_sequence]))
        return True
    else:
        print("System is in an UNSAFE state. Deadlock may occur!")
        return False

if __name__ == "__main__":
    # Example input
    available = [3, 3, 2]  # Available instances of each resource
    max_demand = [
        [7, 5, 3],  # P0
        [3, 2, 2],  # P1
        [9, 0, 2],  # P2
        [2, 2, 2],  # P3
        [4, 3, 3]   # P4
    ]
    allocation = [
        [0, 1, 0],  # P0
        [2, 0, 0],  # P1
        [3, 0, 2],  # P2
        [2, 1, 1],  # P3
        [0, 0, 2]   # P4
    ]

    print("--- Banker's Algorithm Deadlock Avoidance ---")
    is_safe_state(available, max_demand, allocation)
