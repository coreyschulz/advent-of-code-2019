import sys
from day3_data import l1Data
from day3_data import l2Data

line1Points = {}
line2Points = {}

def addPointToDict(dictionary, x, y, numSteps):
    if (x, y) not in dictionary.keys():
        dictionary[(x, y)] = numSteps

def calculatePointsVisited(data, pointSet):
    x = 0
    y = 0
    numSteps = 0 

    for dataPoint in data:
        direction = dataPoint[0]
        amount = int(dataPoint[1:])
        
        if direction == "L":
            for i in range(amount):
                numSteps += 1
                x -= 1
                addPointToDict(pointSet, x, y, numSteps)
                
        elif direction == "R":
            for i in range(amount):
                numSteps += 1
                x += 1
                addPointToDict(pointSet, x, y, numSteps)

        elif direction == "D":
            for i in range(amount):
                numSteps += 1
                y -= 1
                addPointToDict(pointSet, x, y, numSteps)

        elif direction == "U":
            for i in range(amount):
                numSteps += 1
                y += 1
                addPointToDict(pointSet, x, y, numSteps)
                

calculatePointsVisited(l1Data, line1Points)
calculatePointsVisited(l2Data, line2Points) 

minDistance = sys.maxsize

## Solve part 1:

for point in line1Points.keys():
    if point in line2Points.keys():
       tempDist = abs(point[1]) + abs(point[0])
       if tempDist < minDistance:
           minDistance = tempDist

print(minDistance)

minTotalSteps = sys.maxsize 

## Solve part 2:
for point in line1Points.keys():
    if point in line2Points.keys():
        tempHops = line1Points[point] + line2Points[point]
        if tempHops < minTotalSteps:
            minTotalSteps = tempHops

print(minTotalSteps) 
        

