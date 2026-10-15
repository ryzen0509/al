##Q.1

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

print("BFS Traversal:")
bfs(graph, 'A')

##Q.2

students = ["Amit", "Rahul", "Priya", "Neha"]

def is_student(name):
    return name in students

print("Is Amit a student?", is_student("Amit"))
print("Is Rohan a student?", is_student("Rohan"))

all_students = all(is_student(name) for name in students)
print("All names are students:", all_students)

exists_student = any(is_student(name) for name in ["Rohan", "Priya"])
print("At least one student exists:", exists_student)