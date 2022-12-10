import math

segments = [(0,0) for _ in range(10)]
tailVisited = []

cmds = [[x for x in line.strip().split(" ")] for line in open("input.txt", "r")]

def getDirection(dir):
    match dir:
        case "U":
            return (0, 1)
        case "D":
            return (0, -1)
        case "L":
            return (-1, 0)
        case "R":
            return (1, 0)

def calculateMove(pos1, pos2):
    if(math.dist(pos1, pos2) > math.sqrt(2)):
        #move necessary
        if(pos2[0] - pos1[0] > 0):
            dx = 1
        elif(pos2[0] - pos1[0] < 0):
            dx = -1
        else:
            dx = 0
 
        if(pos2[1] - pos1[1] > 0):
            dy = 1
        elif(pos2[1] - pos1[1] < 0):
            dy = -1
        else:
            dy = 0

        return (dx, dy)
    else:
        return (0,0)
    
for cmd in cmds:
    dir = getDirection(cmd[0])
    for i in range(int(cmd[1])):
        segments[0] = (segments[0][0] + dir[0], segments[0][1] + dir[1])
        for i in range(1, len(segments)):
            move = calculateMove(segments[i], segments[i-1])
            segments[i] = (segments[i][0] + move[0], segments[i][1] + move[1])

        if(segments[9] not in tailVisited):
            print(segments[9])
            tailVisited.append(segments[9])

print(len(tailVisited))