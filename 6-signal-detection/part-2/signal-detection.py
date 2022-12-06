data = [line.strip() for line in open("..\input.txt", "r")]

for line in data:
    for i in range(13, len(line)):
        checkSet = set(line[i-13:i+1])
        if len(checkSet) == 14:
            print(i+1)
            break