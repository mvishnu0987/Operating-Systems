def cscan_disk_scheduling(requests, head_start, disk_size):
    requests = sorted(requests)
    total_movement = 0
    sequence = [head_start]

    print(f"Initial Head Position: {head_start}")

    # Requests above and below the head
    up_requests = [r for r in requests if r >= head_start]
    down_requests = [r for r in requests if r < head_start]

    # Move up and service requests
    for track in up_requests:
        total_movement += abs(track - head_start)
        head_start = track
        sequence.append(track)

    # Move to end of disk
    if up_requests and head_start != disk_size - 1:
        total_movement += abs((disk_size - 1) - head_start)
        head_start = disk_size - 1
        sequence.append(head_start)

    # Jump to start of disk (0)
    total_movement += head_start  # from current head to 0
    head_start = 0
    sequence.append(head_start)

    # Service remaining requests
    for track in down_requests:
        total_movement += abs(track - head_start)
        head_start = track
        sequence.append(track)

    print(f"\nSequence of head movement: {sequence}")
    print(f"Total Head Movement: {total_movement}")

if __name__ == "__main__":
    requests = [82, 170, 43, 140, 24, 16, 190]  # Disk I/O requests
    head_start = 50  # Initial head position
    disk_size = 200  # Total number of tracks

    cscan_disk_scheduling(requests, head_start, disk_size)
