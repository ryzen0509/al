##Q.1

def objective(x):
    return -(x - 3) ** 2 + 9

def hill_climbing(start):
    current = start

    while True:
        left = current - 1
        right = current + 1

        current_value = objective(current)

        if objective(left) > current_value:
            current = left

        elif objective(right) > current_value:
            current = right

        else:
            break

    return current, objective(current)


start = 0

best_x, best_value = hill_climbing(start)

print("Maximum value of x:", best_x)
print("Maximum value:", best_value)

##Q.2

facts = {"rain", "wet_ground"}

rules = [
    ({"rain"}, "wet_ground"),
    ({"wet_ground"}, "slippery"),
    ({"slippery"}, "drive_carefully")
]

def forward_chaining(facts, rules):
    new_fact_added = True

    while new_fact_added:
        new_fact_added = False

        for conditions, conclusion in rules:
            if conditions.issubset(facts):
                if conclusion not in facts:
                    facts.add(conclusion)
                    print("New Fact:", conclusion)
                    new_fact_added = True

    return facts


result = forward_chaining(facts, rules)

print("\nFinal Facts:")
print(sorted(result))