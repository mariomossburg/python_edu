def is_safe_state(alloc, max_demand, avail):
    need = [[max_demand[i][j] - alloc[i][j] for j in range(len(avail))] for i in range(len(alloc))]
    finish = [False] * len(alloc)
    work = avail[:]

    while True:
        found = False
        for i in range(len(alloc)):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(len(avail))):
                for j in range(len(avail)):
                    work[j] += alloc[i][j]
                finish[i] = True
                found = True
        if not found:
            break

    return all(finish)

if __name__ == "__main__":
    alloc = [[0, 1, 0],
             [2, 0, 0],
             [3, 0, 2],
             [2, 1, 1],
             [0, 0, 2]]
    
    max_demand = [[7, 5, 3],
                  [3, 2, 2],
                  [9, 0, 2],
                  [2, 2, 2],
                  [4, 3, 3]]
    
    avail = [3, 3, 2]

    print("Deadlock Detection - Is the system in a safe state?\n")
    print(f"{'Process':<8} {'Allocation':<20} {'Max Demand':<20}")
    for i, (a, m) in enumerate(zip(alloc, max_demand)):
        print(f"P{i:<7} {str(a):<20} {str(m):<20}")

    safe = is_safe_state(alloc, max_demand, avail)
    print("\nAvailable Resources:", avail)
    print("Safe State:" , safe)


# Notes:
# alloc = currently allocated resources for each process (matrix)
# max_demand = maximum demand of each resource per process (matrix)
# avail = currently available resources (vector)
# need = resources still needed by each process (max_demand - alloc)
# finish = tracks which processes can finish safely
# work = simulated available resources during the check
# The algorithm checks if the system is in a safe state (no deadlock) by simulating resource allocation.
