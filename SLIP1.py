#Q.1

from collections import deque

queue = deque(["Monkey at Door"])
visited = []

while queue:
    state = queue.popleft()

    if state not in visited:
        visited.append(state)
        print(state)

        if state == "Monkey at Door":
            queue.append("Monkey at Box")

        elif state == "Monkey at Box":
            queue.append("Box Under Banana")

        elif state == "Box Under Banana":
            queue.append("Monkey Climbs Box")

        elif state == "Monkey Climbs Box":
            queue.append("Monkey Gets Banana")

        elif state == "Monkey Gets Banana":
            print("\nGoal: Banana Obtained!")
            break

##Q.2
import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 1), ('E', 5)],
    'C': [('D', 2), ('E', 3)],
    'D': [('E', 2)],
    'E': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 0
}

def astar(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            print("Shortest Path:", path)
            print("Total Cost:", g)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]

                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbour,
                     path + [neighbour])
                )

    print("Path not found")

astar('A', 'E')
