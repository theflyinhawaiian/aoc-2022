import bisect

file = open("input.txt", 'r')

currCount = 0
maxCounts = [0,0,0]

done = False

while(not done):
    line = file.readline()
    if(line == "\n" or line == ""):
        if(min(maxCounts) < currCount):
            print(f"adding new count {currCount}")
            bisect.insort(maxCounts, currCount)
            maxCounts.pop(0)
        currCount = 0
        if(line == ""):
            done = True
        continue

    num = int(line.strip())
    currCount = currCount + num

file.close()

sum = 0
for cals in maxCounts:
    sum = sum + cals

print(sum)