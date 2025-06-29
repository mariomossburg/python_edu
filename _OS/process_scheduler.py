import queue # FIFO DS

class Process:
    def __init__(self, pid, burst, priority):
        self.pid = pid
        self.burst = burst
        self.priority = priority

def round_robin(processes, time_quantum):
    q = queue.Queue() 
    for p in processes:
        q.put(p) # put() == add
    
    print(f"{'Process':<10} {'Burst Left':<12} {'Action':<30} {'Queue State'}")
    print("-" * 70)
    
    
    # while q: # not the same as below, a queue doesn't define truthiness, so it doesn't safely show if empty
    while not q.empty():
        p = q.get()
        run_time = min(time_quantum, p.burst)
        p.burst -= run_time
        action = f"Ran for {run_time} units"
        queue_state = [proc.pid for proc in list(q.queue)]
        
        if p.burst > 0:
            q.put(p)
            print(f"{p.pid:<10} {p.burst:<12} {action + ', re-queued':<30} {queue_state}")
        else:
            print(f"{p.pid:<10} {0:<12} {action + ', finished':<30} {queue_state}")

if __name__ == "__main__":
    processes = [
        Process("P1", 10, 1),
        Process("P2", 4, 2),
        Process("P3", 6, 1),
        Process("P4", 5, 2)
    ]
    print("Round Robin Scheduling (Time Quantum = 3):\n")
    round_robin(processes, time_quantum=3)



# Notes:
# A queue is a FIFO (First-In, First-Out) data structure — 
# like a at the amazon store, where the first person to get in line is the first served.

# pid = process identifier (name or number)
# burst = amount of CPU time required by the process
# priority = scheduling priority (not used here but important in other algorithms)
# round_robin simulates the CPU giving fixed time slices (quantum) to each process cyclically.
# If a process is not finished in one quantum, it goes back to the end of the queue.
