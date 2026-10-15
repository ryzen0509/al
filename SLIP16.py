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

def dls(node, goal, limit, path):
    print(node, end=" ")

    if node == goal:
        return True

    if limit <= 0:
        return False

    for neighbour in graph[node]:
        if dls(neighbour, goal, limit - 1, path):
            return True

    return False


start = 'A'
goal = 'G'
limit = 2

print("DLS Traversal:")

if dls(start, goal, limit, []):
    print("\nGoal Found:", goal)
else:
    print("\nGoal Not Found")

##Q.2

facts = {
    "fever",
    "cough"
}

rules = {
    "flu": ["fever", "cough"],
    "rest_needed": ["flu"]
}


def backward_chaining(goal):
    if goal in facts:
        return True

    if goal in rules:
        for condition in rules[goal]:
            if not backward_chaining(condition):
                return False

        return True

    return False


goal = "rest_needed"

if backward_chaining(goal):
    print("Goal", goal, "is True")
else:
    print("Goal", goal, "is False")