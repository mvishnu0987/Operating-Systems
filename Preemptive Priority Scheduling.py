def preemptive_priority_scheduling(processes, burst_time, priority, arrival_time):
    n = len(processes)
    remaining_time = burst_time[:]   # copy burst times
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n

    time = 0
    completed = 0
    prev = -1

    while completed != n:
        # Find process with highest priority among those arrived
        idx = -1
        highest_priority = float('inf')
        for i in range(n):
            if arrival_time[i] <= time and remaining_time[i] > 0:
                if priority[i] < highest_priority:
                    highest_priority = priority[i]
                    idx = i
                elif priority[i] == highest_priority:
                    # Tie-break: earlier arrival
                    if arrival_time[i] < arrival_time[idx]:
                        idx = i

        if idx != -1:
            # Run this process for 1 unit
            remaining_time[idx] -= 1

            if remaining_time[idx] == 0:  # finished
                completed += 1
                completion_time[idx] = time + 1
                turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
                waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
        time += 1

    # Averages
    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    # Print table
    print("\nProcess\tAT\tBT\tPriority\tWT\tTAT")
    for i in range(n):
        print(f"P{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{priority[i]}\t\t{waiting_time[i]}\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    processes = [i + 1 for i in range(n)]
    burst_time = []
    priority = []
    arrival_time = []

    for i in range(n):
        at = int(input(f"Enter Arrival Time for Process P{i+1}: "))
        bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
        pr = int(input(f"Enter Priority for Process P{i+1} (lower number = higher priority): "))
        arrival_time.append(at)
        burst_time.append(bt)
        priority.append(pr)

    preemptive_priority_scheduling(processes, burst_time, priority, arrival_time)
