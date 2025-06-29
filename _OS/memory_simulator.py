from collections import deque # used for frame list (FIFO)

"""View realtime memory usage"""
# vm_stat # for mac


# The deque with maxlen=3 is a bus with 3 seats.
# Each page request is a person trying to board.
# If already on the bus → hit (no action).
# If not on the bus and it's full → oldest person gets off (evicted), new one boards.
# Our PageTable simulates RAM holding memory pages.
# If RAM is full, page eviction occurs — oldest/least-used pages are written to SSD




class PageTable:
    def __init__(self, frame_count):
        self.frames = deque(maxlen=frame_count) # FIFO fixed-size buffer
        

    def load_page(self, page_number):
        if page_number in self.frames:
            action = f"Page {page_number} hit"
        else:
            evicted = self.frames[0] if len(self.frames) == self.frames.maxlen else None
            self.frames.append(page_number)
            action = f"Loaded page {page_number}"
            if evicted is not None:
                action += f", evicted {evicted}"
        return list(self.frames), action

def simulate_paging(page_table, page_sequence):
    print(f"{'Page':<8} {'Action':<35} {'Frame State'}")
    print("-" * 65)
    
    for page in page_sequence:
        frame_state, action = page_table.load_page(page)
        print(f"{page:<8} {action:<35} {frame_state}")

if __name__ == "__main__":
    pt = PageTable(frame_count=3)
    pages = [1, 2, 3, 2, 4, 1, 5, 2]
    
    print("Paging Simulation (FIFO replacement):\n")
    simulate_paging(pt, pages)
    
    # Notes:
# A deque with maxlen is used as a FIFO frame buffer — once full, it auto-evicts the oldest page.
# A page is like a chunk of memory/data needed by a program.
# page_sequence = order in which pages are requested (simulated memory accesses)
# If a page is already in frames → it's a hit (no loading needed)
# If not → it's loaded and possibly evicts the oldest page (FIFO)
# This simulates memory management with paging, like an OS deciding which memory pages stay in RAM.
