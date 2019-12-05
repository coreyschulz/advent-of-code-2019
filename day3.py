import sys
from day3_data import l1Data
from day3_data import l2Data

line1Points = set()
line2Points = set()

def calculatePointsVisited(data, pointSet):
    x = 0
    y = 0

    for dataPoint in data:
        direction = dataPoint[0]
        amount = int(dataPoint[1:])
        
        if direction == "L":
            for i in range(amount):
                x -= 1
                pointSet.add((x, y))
                
        elif direction == "R":
            for i in range(amount):
                x += 1
                pointSet.add((x, y)) 

        elif direction == "D":
            for i in range(amount):
                y -= 1
                pointSet.add((x, y))

        elif direction == "U":
            for i in range(amount):
                y += 1
                pointSet.add((x, y))
                

calculatePointsVisited(l1Data, line1Points)
calculatePointsVisited(l2Data, line2Points) 

minDistance = sys.maxsize

for point in line1Points:
    if point in line2Points:
       tempDist = abs(point[1]) + abs(point[0])
       if tempDist < minDistance:
           minDistance = tempDist

print(minDistance)

