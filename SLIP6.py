##Q.1

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS Traversal:", dfs(graph, 'A'))

##Q.2

from sklearn.svm import SVC

X = [
    [1, 2],
    [2, 3],
    [5, 5]
]

y = [0, 0, 1]

X_test = [[4, 4]]

model = SVC(kernel='rbf')

model.fit(X, y)

prediction = model.predict(X_test)

print("Test Input:", X_test)
print("Predicted Class:", prediction)