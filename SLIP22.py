##Q.1

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = 3

print("Tower of Hanoi Solution:")
tower_of_hanoi(n, 'A', 'B', 'C')

##Q.2

weather = input("Enter weather (sunny/rainy): ").lower()
temperature = input("Enter temperature (hot/cold): ").lower()

if weather == "rainy":
    print("Decision: Carry an umbrella")

elif weather == "sunny" and temperature == "hot":
    print("Decision: Wear light clothes")

elif weather == "sunny" and temperature == "cold":
    print("Decision: Wear warm clothes")

else:
    print("Decision: Check weather conditions")