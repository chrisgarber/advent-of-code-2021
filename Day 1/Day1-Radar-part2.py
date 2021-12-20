import os
import queue
radar_path = os.path.join(os.path.dirname(__file__), "Day1Input.txt")

increasingWindows = 0
windowSize = 3
priorWindow = queue.Queue(windowSize)
with open(radar_path, "r") as radar_file:
    for line in radar_file:
        lineval = int(line)
        if priorWindow.full() and priorWindow.get() < lineval:
            increasingWindows += 1
        priorWindow.put(lineval)
 
print(increasingWindows)