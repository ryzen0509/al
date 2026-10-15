##Q.1

from collections import deque

def bfs_traversal(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    traversal_order = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'

result = bfs_traversal(graph, start_node)

print("Graph:", graph)
print("BFS Traversal starting from", start_node, ":", result)

##Q.2

p = True
q = False

print("P =", p)
print("Q =", q)

print("P AND Q =", p and q)
print("P OR Q =", p or q)
print("NOT P =", not p)
print("NOT Q =", not q)