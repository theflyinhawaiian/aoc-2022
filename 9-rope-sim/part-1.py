import math

headPos = (0,0)
tailPos = (0,0)
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
    

for cmd in cmds:
    dir = getDirection(cmd[0])
    for i in range(int(cmd[1])):
        nextPos = (headPos[0] + dir[0], headPos[1] + dir[1])
        if(math.dist(tailPos, nextPos) > math.sqrt(2)):
            tailPos = headPos
        headPos = nextPos
        if(tailPos not in tailVisited):
            tailVisited.append(tailPos)

print(len(tailVisited))