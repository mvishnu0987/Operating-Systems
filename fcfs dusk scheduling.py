def fcfs_disk_scheduling(requests, head_start):
    head = head_start
    total_movement = 0
    sequence = [head]

    print(f"Initial Head Position: {head}")

    for track in requests:
        movement = abs(track - head)
        total_movement += movement
        head = track
        sequence.append(head)
        print(f"Move from {sequence[-2]} to {head} -> Movement = {movement}")

    print(f"\nTotal Head Movement: {total_movement}")
    print(f"Sequence of head movement: {sequence}")

if __name__ == "__main__":
    requests = [82, 170, 43, 140, 24, 16, 190]  # Disk I/O requests
    head_start = 50  # Initial head position

    fcfs_disk_scheduling(requests, head_start)
