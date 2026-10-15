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

def astar(start, goal):
    queue = [(h[start], 0, start, [start])]
    best_cost = {start: 0}

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            return path, g

        if g > best_cost.get(node, float('inf')):
            continue

        for neighbour, cost in graph[node]:
            new_g = g + cost

            if new_g < best_cost.get(neighbour, float('inf')):
                best_cost[neighbour] = new_g
                new_f = new_g + h[neighbour]

                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbour, path + [neighbour])
                )

    return None, float('inf')


path, cost = astar('A', 'G')

if path:
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("Path not found")

##Q.2

import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
])

y = np.array([2, 4, 6, 8, 10])

model = MLPRegressor(
    hidden_layer_sizes=(5,),
    activation="identity",
    solver="lbfgs",
    max_iter=2000,
    random_state=42
)

model.fit(X, y)

y_pred = model.predict(X)

print("Actual Values:", y)
print("Predicted Values:", np.round(y_pred, 2))

mse = mean_squared_error(y, y_pred)

print("Mean Squared Error:", round(mse, 4))