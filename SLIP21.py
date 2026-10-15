##Q.1

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}


def dls(node, goal, depth):
    print(node, end=" ")

    if node == goal:
        return True

    if depth == 0:
        return False

    for neighbour in graph[node]:
        if dls(neighbour, goal, depth - 1):
            return True

    return False


def ids(start, goal, max_depth):
    for depth in range(max_depth + 1):
        print("\nDepth:", depth)

        if dls(start, goal, depth):
            print("\nGoal Found:", goal)
            return

    print("\nGoal Not Found")


ids('A', 'G', 3)

##Q.2

from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

X, y = make_blobs(
    n_samples=200,
    centers=3,
    n_features=2,
    cluster_std=1.5,
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Actual Values:")
print(y_test[:10])

print("\nPredicted Values:")
print(y_pred[:10])

print("\nAccuracy:", accuracy_score(y_test, y_pred))

new_data = [
    [-2, 5],
    [0, 0],
    [6, -0.3]
]

prediction = model.predict(new_data)

print("\nNew Data Predictions:")
print(prediction)