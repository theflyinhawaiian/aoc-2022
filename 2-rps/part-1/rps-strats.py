def processScore(a,b):
    if(a == b):
        return 3 + b

    if(a == 1):
        if(b == 2):
            return 8
        else:
            return 3
    elif(a == 2):
        if(b == 1):
            return 1
        else:
            return 9
    elif(a == 3):
        if(b == 1):
            return 7
        else:
            return 2

values = { "A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3 }

file = open("..\input.txt", 'r')

line = file.readline()
score = 0

while(line != ""):
    actions = line.split(" ")
    a = values[actions[0].strip()]
    b = values[actions[1].strip()]
    score = score + processScore(a,b)
    line = file.readline()

file.close()
print(score)