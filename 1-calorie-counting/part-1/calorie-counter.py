elves = []

file = open("input.txt", 'r')

line = file.readline()

index = 0
currCount = 0
maxCount = 0
elves.append([])

while(line != ""):
    if(line == "\n"):
        currCount = 0
        index = index + 1
        elves.append([])
        line = file.readline()
        continue

    num = int(line.strip())
    currCount = currCount + num
    if(maxCount < currCount):
        maxCount = currCount

    elves[index].append(num)

    line = file.readline()

file.close()
print(maxCount)