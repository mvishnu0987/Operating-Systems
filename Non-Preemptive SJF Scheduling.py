def sjf_non_preemptive(processes, arrival_time, burst_time):
    n = len(processes)
    completed = 0
    time = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    visited = [False] * n

    while completed != n:
        # Find the process with the shortest burst time among arrived processes
        idx = -1
        min_bt = float('inf')
        for i in range(n):
            if arrival_time[i] <= time and not visited[i]:
                if burst_time[i] < min_bt:
                    min_bt = burst_time[i]
                    idx = i
                elif burst_time[i] == min_bt:  # tie-breaker: earlier arrival
                    if arrival_time[i] < arrival_time[idx]:
                        idx = i

        if idx != -1:
            # Execute the chosen process
            time += burst_time[idx]
            completion_time[idx] = time
            turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
            waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
            visited[idx] = True
            completed += 1
        else:
            time += 1  # if no process has arrived yet, move time forward

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
    n = int(input("Enter the number of processes: "))
    processes = [i + 1 for i in range(n)]
    arrival_time = []
    burst_time = []

    for i in range(n):
        at = int(input(f"Enter Arrival Time for Process P{i+1}: "))
        bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
        arrival_time.append(at)
        burst_time.append(bt)

    sjf_non_preemptive(processes, arrival_time, burst_time)
