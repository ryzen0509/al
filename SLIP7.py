##Q.1

import heapq

graph = {
    'V1': [('V2', 1), ('V3', 4)],
    'V2': [('V4', 2), ('V5', 5)],
    'V3': [('V5', 1)],
    'V4': [('V6', 3)],
    'V5': [('V6', 2)],
    'V6': []
}

heuristic = {
    'V1': 5,
    'V2': 4,
    'V3': 3,
    'V4': 2,
    'V5': 1,
    'V6': 0
}

def astar(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    best_cost = {start: 0}

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if g > best_cost.get(node, float('inf')):
            continue

        if node == goal:
            print("Shortest Path:", path)
            print("Total Cost:", g)
            return

        for neighbor, cost in graph[node]:
            new_g = g + cost

            if new_g < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_g
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    print("Path not found")

astar('V1', 'V6')

##Q.2

colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

assignment = {}

def is_safe(node, color):
    for neighbor in graph[node]:
        if assignment.get(neighbor) == color:
            return False
    return True

def solve(nodes):
    if not nodes:
        return True

    node = nodes[0]

    for color in colors:
        if is_safe(node, color):
            assignment[node] = color

            if solve(nodes[1:]):
                return True

            del assignment[node]

    return False

if solve(list(graph.keys())):
    print("Map Coloring Solution:")

    for node, color in assignment.items():
        print(node, ":", color)
else:
    print("No solution exists")