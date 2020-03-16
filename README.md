# Path-Planner

## Motivation
In a simple robot navigation problem, a GPS device is used to locate the robot inside an environment, or a preloaded set of maps, or even using Simultaneous Localization and Mapping (SLAM) in complex applications, but once the robot realizes the environment and constrains round it, it starts to generate a path using algorithms like A* or BFS, and this computation could be done using Raspberry-Pi communication with another microcontroller (Mc) to drive the actuators. In this repo JSON binary text file is used as a shared resource for communication between the two Mcs. In practice this approach is not frequently used. However it gives an intuition on how to implement a simple path planner algorithm.

## How to use the code
Inputs: Binary JSON text file with the map configured as follows:
"1": Obstacle
"0": Free Space
"S": Robot Starting Point
"G": Goal

Json file example:
map: S1
     0G

JSON_File: [{"0":"S","1":"1"},
            {"0":"0","1":"G"}]

Also, there are two helper functions to generate and print a random map if you want to give it a shot.