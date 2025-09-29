def fifo_paging(pages, frame_size):
    frames = []
    page_faults = 0

    print("Page Reference\tFrames\t\tPage Fault")
    for page in pages:
        if page not in frames:
            page_faults += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                # Remove the oldest page (FIFO)
                frames.pop(0)
                frames.append(page)
            fault = "Yes"
        else:
            fault = "No"
        print(f"{page}\t\t{frames}\t{fault}")

    print(f"\nTotal Page Faults: {page_faults}")

if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]  # Page reference string
    frame_size = 3  # Number of frames in memory

    fifo_paging(pages, frame_size)
