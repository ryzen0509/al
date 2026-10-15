##Q.1

def f(x):
    return -x**2 + 4*x


def hill_climbing(start):
    x = start

    while True:
        left = x - 1
        right = x + 1

        if f(left) > f(x):
            x = left

        elif f(right) > f(x):
            x = right

        else:
            break

    return x, f(x)


start = 0

best_x, maximum = hill_climbing(start)

print("Maximum value of x:", best_x)
print("Maximum value of F(x):", maximum)

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

# Unsupervised Learning
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

kmeans.fit(X)

print("\nUnsupervised Learning Cluster Labels:")
print(kmeans.labels_[:10])