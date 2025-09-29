def optimal_paging(pages, frame_size):
    frames = []
    page_faults = 0

    print("Page Reference\tFrames\t\tPage Fault")
    for i, page in enumerate(pages):
        if page not in frames:
            page_faults += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                # Find the page to replace (optimal)
                future_uses = {}
                for f in frames:
                    if f in pages[i+1:]:
                        future_uses[f] = pages[i+1:].index(f)
                    else:
                        future_uses[f] = float('inf')  # Not used again
                # Replace the page that is used farthest in future
                page_to_replace = max(future_uses, key=future_uses.get)
                frames[frames.index(page_to_replace)] = page
            fault = "Yes"
        else:
            fault = "No"

        print(f"{page}\t\t{frames}\t{fault}")

    print(f"\nTotal Page Faults: {page_faults}")

if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]  # Page reference string
    frame_size = 3  # Number of frames in memory

    optimal_paging(pages, frame_size)
