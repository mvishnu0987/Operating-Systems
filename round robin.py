from collections import deque

def round_robin(processes, arrival_time, burst_time, quantum):
    n = len(processes)
    remaining_time = burst_time[:]   # copy burst times
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n

    time = 0
    queue = deque()
    visited = [False] * n
    completed = 0

    # Start simulation
    while completed != n:
        # Add newly arrived processes to queue
        for i in range(n):
            if arrival_time[i] <= time and not visited[i]:
                queue.append(i)
                visited[i] = True

        if queue:
            idx = queue.popleft()

            # Execute for min(quantum, remaining time)
            exec_time = min(quantum, remaining_time[idx])
            remaining_time[idx] -= exec_time
            time += exec_time

            # Add newly arrived processes during execution
            for i in range(n):
                if arrival_time[i] <= time and not visited[i]:
                    queue.append(i)
                    visited[i] = True

            if remaining_time[idx] == 0:  # process finished
                completed += 1
                completion_time[idx] = time
                turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
                waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
            else:
                queue.append(idx)  # put back into queue
        else:
            time += 1  # idle CPU if no process is ready

    # Averages
    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    # Print results
    print("\nProcess\tAT\tBT\tCT\tWT\tTAT")
    for i in range(n):
        print(f"P{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{completion_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    processes = [i + 1 for i in range(n)]
    arrival_time = []
    burst_time = []

    for i in range(n):
        at = int(input(f"Enter Arrival Time for Process P{i+1}: "))
        bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
        arrival_time.append(at)
        burst_time.append(bt)

    quantum = int(input("Enter Time Quantum: "))

    round_robin(processes, arrival_time, burst_time, quantum)
