import timeit
from collections import deque

# ==============================================================
# SLE-2: EMPIRICAL PERFORMANCE ANALYSIS
# Comparison: BFS vs DFS
# Best Case, Average Case and Worst Case
# ==============================================================

NUM_NODES = 1200
NUMBER_OF_RUNS = 3


# --------------------------------------------------------------
# Create Graph
# --------------------------------------------------------------
def create_graph():
    graph = {i: [] for i in range(NUM_NODES)}

    # Each node is connected to the next 4 nodes
    for i in range(NUM_NODES):
        for j in range(1, 5):
            if i + j < NUM_NODES:
                graph[i].append(i + j)

    return graph


graph = create_graph()


# --------------------------------------------------------------
# BFS - Breadth First Search
# --------------------------------------------------------------
def bfs(graph, start, goal):

    queue = deque([start])
    visited = {start}
    nodes_expanded = 0

    while queue:

        node = queue.popleft()
        nodes_expanded += 1

        # Small computation for measurable execution time
        value = 0
        for i in range(2000):
            value += i

        if node == goal:
            return True, nodes_expanded

        for neighbour in graph[node]:

            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return False, nodes_expanded


# --------------------------------------------------------------
# DFS - Depth First Search
# --------------------------------------------------------------
def dfs(graph, start, goal):

    stack = [start]
    visited = {start}
    nodes_expanded = 0

    while stack:

        node = stack.pop()
        nodes_expanded += 1

        # Small computation for measurable execution time
        value = 0
        for i in range(2000):
            value += i

        if node == goal:
            return True, nodes_expanded

        # Reverse order to control DFS traversal order
        for neighbour in reversed(graph[node]):

            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)

    return False, nodes_expanded


# --------------------------------------------------------------
# Profile Algorithm using timeit
# --------------------------------------------------------------
def profile_algorithm(algorithm, start, goal):

    def run_algorithm():
        return algorithm(graph, start, goal)

    times = timeit.repeat(
        stmt=run_algorithm,
        repeat=NUMBER_OF_RUNS,
        number=1
    )

    # Execute once to obtain nodes expanded
    goal_found, nodes_expanded = algorithm(
        graph,
        start,
        goal
    )

    times_ms = [t * 1000 for t in times]

    average_time = sum(times_ms) / len(times_ms)

    return (
        times_ms,
        average_time,
        nodes_expanded,
        goal_found
    )


# --------------------------------------------------------------
# Print Case Result
# --------------------------------------------------------------
def print_case_result(case_name, start, goal):

    print("\n" + "-" * 70)
    print(case_name)
    print("-" * 70)

    print(f"Start Node : {start}")
    print(f"Goal Node  : {goal}")

    # ==========================================================
    # BFS
    # ==========================================================

    bfs_times, bfs_avg, bfs_nodes, bfs_found = profile_algorithm(
        bfs,
        start,
        goal
    )

    print("\nBFS - Breadth First Search")

    for i in range(NUMBER_OF_RUNS):
        print(
            f"Run {i + 1}: "
            f"Time = {bfs_times[i]:.5f} ms, "
            f"Nodes Expanded = {bfs_nodes}"
        )

    print(f"Average Time = {bfs_avg:.5f} ms")
    print(f"Goal Found   = {bfs_found}")

    # ==========================================================
    # DFS
    # ==========================================================

    dfs_times, dfs_avg, dfs_nodes, dfs_found = profile_algorithm(
        dfs,
        start,
        goal
    )

    print("\nDFS - Depth First Search")

    for i in range(NUMBER_OF_RUNS):
        print(
            f"Run {i + 1}: "
            f"Time = {dfs_times[i]:.5f} ms, "
            f"Nodes Expanded = {dfs_nodes}"
        )

    print(f"Average Time = {dfs_avg:.5f} ms")
    print(f"Goal Found   = {dfs_found}")

    # ==========================================================
    # Comparison
    # ==========================================================

    print("\nComparison:")

    print(f"BFS Average Time : {bfs_avg:.5f} ms")
    print(f"DFS Average Time : {dfs_avg:.5f} ms")

    print(f"BFS Nodes        : {bfs_nodes}")
    print(f"DFS Nodes        : {dfs_nodes}")

    if bfs_avg < dfs_avg:
        print("Faster Algorithm : BFS")

    elif dfs_avg < bfs_avg:
        print("Faster Algorithm : DFS")

    else:
        print("Faster Algorithm : Same")

    if bfs_nodes < dfs_nodes:
        print("Fewer Nodes      : BFS")

    elif dfs_nodes < bfs_nodes:
        print("Fewer Nodes      : DFS")

    else:
        print("Nodes Expanded   : Same")


# ==============================================================
# MAIN PROGRAM
# ==============================================================

print("=" * 70)
print("SLE-2: EMPIRICAL PERFORMANCE ANALYSIS")
print("Comparison: BFS vs DFS")
print("Best Case, Average Case and Worst Case")
print("=" * 70)

print("\nProblem:")
print(f"Number of Nodes = {NUM_NODES}")
print("Start Node      = 0")
print(f"Number of Runs  = {NUMBER_OF_RUNS}")
print("Timing Tool     = timeit")


# ==============================================================
# BFS CASE ANALYSIS
# ==============================================================

print("\n" + "=" * 70)
print("BFS CASE ANALYSIS")
print("=" * 70)

# BFS Best Case
print_case_result(
    "BFS - BEST CASE",
    0,
    1
)

# BFS Average Case
print_case_result(
    "BFS - AVERAGE CASE",
    0,
    600
)

# BFS Worst Case
print_case_result(
    "BFS - WORST CASE",
    0,
    1199
)


# ==============================================================
# DFS CASE ANALYSIS
# ==============================================================

print("\n" + "=" * 70)
print("DFS CASE ANALYSIS")
print("=" * 70)

# DFS Best Case
print_case_result(
    "DFS - BEST CASE",
    0,
    1
)

# DFS Average Case
print_case_result(
    "DFS - AVERAGE CASE",
    0,
    600
)

# DFS Worst Case
print_case_result(
    "DFS - WORST CASE",
    0,
    1199
)


# ==============================================================
# COMPLETION
# ==============================================================

print("\n" + "=" * 70)
print("PROFILING COMPLETED SUCCESSFULLY")
print("=" * 70)