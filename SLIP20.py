##Q.1

def objective(x):
    return -(x - 3) ** 2 + 9


def hill_climbing(start):
    current = start

    while True:
        left = current - 1
        right = current + 1

        if objective(left) > objective(current):
            current = left

        elif objective(right) > objective(current):
            current = right

        else:
            break

    return current, objective(current)


start = 0

best_x, maximum = hill_climbing(start)

print("Best Value of x:", best_x)
print("Maximum Value:", maximum)

##Q.2

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Supervised Learning Accuracy:")
print(accuracy_score(y_test, y_pred))

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

kmeans.fit(X)

print("\nUnsupervised Learning Cluster Labels:")
print(kmeans.labels_[:10])