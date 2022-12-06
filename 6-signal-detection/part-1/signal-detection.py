data = [line.strip() for line in open("..\input.txt", "r")]

for line in data:
    for i in range(3, len(line)):
        checkSet = set([line[i], line[i-1], line[i-2], line[i-3]])
        if len(checkSet) == 4:
            print(i+1)
            break