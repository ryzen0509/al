##Q.1

import heapq
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 3)],
    'G': []
}

h = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 2,
    'G': 0
}

def best_first_search(start, goal):
    priority_queue = [(h[start], start, [start])]
    visited = set()

    while priority_queue:
        _, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                heapq.heappush(
                    priority_queue,
                    (h[neighbour], neighbour, path + [neighbour])
                )

    return None


path = best_first_search('A', 'G')

if path:
    print("Path Found:", " -> ".join(path))
else:
    print("No Path Found")

##Q.2

p = True
q = False

print("P AND Q:", p and q)

print("P OR Q:", p or q)

print("P IMPLIES Q:", (not p) or q)