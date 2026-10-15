##Q.1

graph = {
    'A': {'AND': [['B', 'C'], ['D']]},
    'B': {'OR': [['E'], ['F']]},
    'C': {'OR': [['G']]},
    'D': {'OR': [['G']]},
    'E': {'OR': []},
    'F': {'OR': []},
    'G': {'OR': []}
}

heuristic = {
    'A': 1,
    'B': 2,
    'C': 2,
    'D': 4,
    'E': 0,
    'F': 0,
    'G': 0
}


def ao_star(node):
    if node not in graph or not graph[node]:
        return heuristic[node]

    options = graph[node].get('AND', [])

    if not options:
        options = graph[node].get('OR', [])

    if not options:
        return heuristic[node]

    best_cost = float('inf')

    for option in options:
        cost = 0

        for child in option:
            cost += 1 + ao_star(child)

        best_cost = min(best_cost, cost)

    heuristic[node] = best_cost
    return best_cost


cost = ao_star('A')

print("Optimal Cost:", cost)
print("Updated Heuristic Values:")

for node, value in heuristic.items():
    print(node, ":", value)

#Q.2

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

values = {
    'D': 3,
    'E': 5,
    'F': 2,
    'G': 9
}


def minimax(node, maximizing):
    if node in values:
        return values[node]

    if maximizing:
        best = float('-inf')

        for child in tree[node]:
            value = minimax(child, False)
            best = max(best, value)

        return best

    else:
        best = float('inf')

        for child in tree[node]:
            value = minimax(child, True)
            best = min(best, value)

        return best


result = minimax('A', True)

print("Optimal Value:", result)