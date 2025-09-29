# Memory Allocation Strategies Simulation in Python

def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        for j, block in enumerate(blocks):
            if block >= process:
                allocation[i] = j
                blocks[j] -= process
                break
    return allocation

def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        best_idx = -1
        for j, block in enumerate(blocks):
            if block >= process:
                if best_idx == -1 or blocks[j] < blocks[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= process
    return allocation

def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        worst_idx = -1
        for j, block in enumerate(blocks):
            if block >= process:
                if worst_idx == -1 or blocks[j] > blocks[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= process
    return allocation

def display_allocation(processes, allocation, strategy_name):
    print(f"\n--- {strategy_name} Memory Allocation ---")
    print("Process No.\tProcess Size\tBlock Allocated")
    for i, block_idx in enumerate(allocation):
        if block_idx != -1:
            print(f"{i+1}\t\t{processes[i]}\t\t{block_idx+1}")
        else:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")

if __name__ == "__main__":
    memory_blocks = [100, 500, 200, 300, 600]
    processes = [212, 417, 112, 426]

    # First Fit
    allocation = first_fit(memory_blocks.copy(), processes)
    display_allocation(processes, allocation, "First Fit")

    # Best Fit
    allocation = best_fit(memory_blocks.copy(), processes)
    display_allocation(processes, allocation, "Best Fit")

    # Worst Fit
    allocation = worst_fit(memory_blocks.copy(), processes)
    display_allocation(processes, allocation, "Worst Fit")
