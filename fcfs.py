def fcfs_scheduling(processes, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Waiting time for the first process is 0
    waiting_time[0] = 0

    # Calculate waiting time for each process
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    # Calculate average WT and TAT
    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    # Display results
    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{processes[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    processes = [i + 1 for i in range(n)]
    burst_time = []

    for i in range(n):
        bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
        burst_time.append(bt)

    fcfs_scheduling(processes, burst_time)
