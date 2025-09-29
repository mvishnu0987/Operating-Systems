def priority_scheduling(processes, burst_time, priority):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Sort processes by priority (lower number = higher priority)
    sorted_processes = sorted(zip(processes, burst_time, priority), key=lambda x: x[2])

    # Reassign after sorting
    processes, burst_time, priority = zip(*sorted_processes)

    # Waiting time for first process = 0
    waiting_time = [0] * n
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

    # Turnaround time = Burst + Waiting
    turnaround_time = [burst_time[i] + waiting_time[i] for i in range(n)]

    # Calculate averages
    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    # Print table
    print("\nProcess\tPriority\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{processes[i]}\t{priority[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

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

    for i in range(n):
        bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
        pr = int(input(f"Enter Priority for Process P{i+1} (lower number = higher priority): "))
        burst_time.append(bt)
        priority.append(pr)

    priority_scheduling(processes, burst_time, priority)
