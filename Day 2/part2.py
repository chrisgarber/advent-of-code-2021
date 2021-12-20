import os
movement_path = os.path.join(os.path.dirname(__file__), "data.txt")

depth = 0
horizontal = 0
aim = 0
with open(movement_path, "r") as movement_file:
    for line in movement_file:
        direction, distance = line.split(" ")
        distance = int(distance)
        if direction == 'up':
            aim -= distance
        if direction == 'down':
            aim += distance
        if direction == 'forward':
            horizontal += distance
            depth += distance * aim

print (depth, horizontal)
print (depth * horizontal)

