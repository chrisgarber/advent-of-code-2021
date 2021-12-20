import os
radar_path = os.path.join(os.path.dirname(__file__), "Day1Input.txt")

increasingLines = 0
priorValue = None
with open(radar_path, "r") as radar_file:
    for line in radar_file:
        lineval = int(line)
        if priorValue and priorValue < lineval:
            increasingLines += 1
        priorValue = lineval
 
print(increasingLines)