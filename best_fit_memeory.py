def best_fit(blocks, processes):
    allocation = [-1] * len(processes)  # Store allocated block index for each process

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

def display_allocation(processes, allocation):
    print("\n--- Best Fit Memory Allocation ---")
    print("Process No.\tProcess Size\tBlock Allocated")
    for i, block_idx in enumerate(allocation):
        if block_idx != -1:
            print(f"{i+1}\t\t{processes[i]}\t\t{block_idx+1}")
        else:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")

if __name__ == "__main__":
    memory_blocks = [100, 500, 200, 300, 600]
    processes = [212, 417, 112, 426]

    allocation = best_fit(memory_blocks.copy(), processes)
    display_allocation(processes, allocation)
