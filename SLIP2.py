##Q.1

from collections import deque

def water_jug():
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x == 2 or y == 2:
            print("Solution:", (x, y))
            return

        states = [
            (4, y),                              
            (x, 3),                              
            (0, y),                              
            (x, 0),                              
            (max(0, x - (3 - y)), min(3, x + y)),
            (min(4, x + y), max(0, y - (4 - x))) 
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

water_jug()

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
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(nodes):
    if not nodes:
        return True

    node = nodes[0]

    for color in colors:
        if is_safe(node, color):
            assignment[node] = color

            if backtrack(nodes[1:]):
                return True

            del assignment[node]

    return False

if backtrack(list(graph.keys())):
    print("Solution Found:")
    for node, color in assignment.items():
        print(node, ":", color)
else:
    print("No solution exists")

##Q.2 OR 

# Game Tree Representation

game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def display_tree(node, level=0):
    print(" " * level + node)

    for child in game_tree[node]:
        display_tree(child, level + 4)

print("Game Tree:")
display_tree('A')