##Q.1

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

print("BFS Traversal:")
bfs(graph, 'A')

##Q.2

class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal Name:", self.name)


class Dog(Animal):
    def sound(self):
        print(self.name, "barks")


class Cat(Animal):
    def sound(self):
        print(self.name, "meows")

dog = Dog("Tommy")
cat = Cat("Kitty")

print("Ontology Example")

dog.display()
dog.sound()

cat.display()
cat.sound()

print("\nRelationship:")
print("Dog is a subclass of Animal")
print("Cat is a subclass of Animal")