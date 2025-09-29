# Worst Fit Memory Allocation in Python

def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)  # stores index of allocated block for each process

    for i, process in enumerate(processes):
        # Find the largest block that can accommodate the process
        worst_idx = -1
        for j, block in enumerate(blocks):
            if block >= process:
                if worst_idx == -1 or blocks[j] > blocks[worst_idx]:
                    worst_idx = j

        # Allocate if found
        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= process

    return allocation

def display_allocation(processes, allocation, blocks):
    print("\n--- Worst Fit Memory Allocation ---")
    print("Process No.\tProcess Size\tBlock Allocated")
    for i, block_idx in enumerate(allocation):
        if block_idx != -1:
            print(f"{i+1}\t\t{processes[i]}\t\t{block_idx+1}")
        else:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")

if __name__ == "__main__":
    # Memory blocks and processes
    memory_blocks = [100, 500, 200, 300, 600]
    processes = [212, 417, 112, 426]

    allocation = worst_fit(memory_blocks.copy(), processes)
    display_allocation(processes, allocation, memory_blocks)
