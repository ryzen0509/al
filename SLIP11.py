##Q.1

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
            best = max(best, minimax(child, False))

        return best

    else:
        best = float('inf')

        for child in tree[node]:
            best = min(best, minimax(child, True))

        return best


def alpha_beta(node, alpha, beta, maximizing):
    if node in values:
        return values[node]

    if maximizing:
        best = float('-inf')

        for child in tree[node]:
            score = alpha_beta(
                child, alpha, beta, False
            )

            best = max(best, score)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for child in tree[node]:
            score = alpha_beta(
                child, alpha, beta, True
            )

            best = min(best, score)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


print("Minimax Value:", minimax('A', True))

print(
    "Alpha-Beta Value:",
    alpha_beta('A', float('-inf'), float('inf'), True)
)

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
    print(goal, "is True")
else:
    print(goal, "is False")