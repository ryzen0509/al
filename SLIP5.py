##Q.1

def dls(graph, node, goal, limit, path=None):
    if path is None:
        path = []

    path = path + [node]

    if node == goal:
        return path

    if limit <= 0:
        return None

    for child in graph.get(node, []):
        result = dls(graph, child, goal, limit - 1, path)

        if result:
            return result

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

result = dls(graph, 'A', 'G', 2)

print("Path found:", result)

##Q.2

from sklearn.svm import SVC

X = [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [4.7, 3.2, 1.3, 0.2],
    [4.6, 3.1, 1.5, 0.2],
    [5.0, 3.6, 1.4, 0.2],
    [7.0, 3.2, 4.7, 1.4],
    [6.4, 3.2, 4.5, 1.5],
    [6.9, 3.1, 4.9, 1.5],
    [6.3, 3.3, 6.0, 2.5],
    [5.8, 2.7, 5.1, 1.9]
]

y = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2]

X_test = [
    [5.2, 3.4, 1.5, 0.2],
    [6.5, 3.0, 4.6, 1.5],
    [6.2, 3.0, 5.2, 2.0]
]

model = SVC(kernel='linear')
model.fit(X, y)

predictions = model.predict(X_test)

print("Predictions:", predictions)