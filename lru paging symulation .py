def lru_paging(pages, frame_size):
    frames = []
    recent_usage = {}  # Track the most recent usage index
    page_faults = 0

    print("Page Reference\tFrames\t\tPage Fault")
    for i, page in enumerate(pages):
        if page not in frames:
            page_faults += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                # Find the least recently used page
                lru_page = min(recent_usage, key=recent_usage.get)
                frames[frames.index(lru_page)] = page
                del recent_usage[lru_page]  # Remove from usage tracking
            fault = "Yes"
        else:
            fault = "No"

        # Update recent usage
        recent_usage[page] = i
        print(f"{page}\t\t{frames}\t{fault}")

    print(f"\nTotal Page Faults: {page_faults}")

if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]  # Page reference string
    frame_size = 3  # Number of frames in memory

    lru_paging(pages, frame_size)
