##Q.1

import heapq
goal = (1, 2, 3, 0)

def heuristic(state):
    distance = 0

    for i in range(4):
        if state[i] != 0:
            goal_pos = goal.index(state[i])
            distance += abs(i // 2 - goal_pos // 2)
            distance += abs(i % 2 - goal_pos % 2)

    return distance

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = zero // 2, zero % 2

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 2 and 0 <= new_col < 2:
            new_pos = new_row * 2 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos],
                new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors

def astar(start):
    queue = [(heuristic(start), 0, start, [start])]
    best_cost = {start: 0}

    while queue:
        f, g, state, path = heapq.heappop(queue)

        if g > best_cost.get(state, float('inf')):
            continue

        if state == goal:
            print("Solution Found:")
            for s in path:
                print(s[0:2])
                print(s[2:4])
                print()
            print("Total Moves:", len(path) - 1)
            return

        for neighbor in get_neighbors(state):
            new_g = g + 1

            if new_g < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_g
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    print("No solution found")

start = (1, 2, 0, 3)

astar(start)

##Q.2

def expert_system():
    print("Simple Expert System")
    print("Enter your weather condition:")

    weather = input("Weather (sunny/rainy): ").lower()

    if weather == "sunny":
        print("Recommendation: Go outside and play.")

    elif weather == "rainy":
        print("Recommendation: Stay indoors and read a book.")

    else:
        print("Unknown weather condition.")

expert_system()