import os
movement_path = os.path.join(os.path.dirname(__file__), "data.txt")

depth = 0
horizontal = 0
with open(movement_path, "r") as movement_file:
    for line in movement_file:
        direction, distance = line.split(" ")
        distance = int(distance)
        if direction == 'up':
            depth -= distance
        if direction == 'down':
            depth += distance
        if direction == 'forward':
            horizontal += distance

print (depth, horizontal)
print (depth * horizontal)

