def processScore(throw, result):
        if(result == 0):
            return 3 + throw

        if(throw == 1):
            if(result == 1):
                return 8
            else:
                return 3
        elif(throw == 2):
            if(result == 1):
                return 9
            else:
                return 1
        elif(throw == 3):
            if(result == 1):
                return 7
            else:
                return 2
    

values = { "A": 1, "B": 2, "C": 3 }
results = { "X": -1, "Y": 0, "Z": 1 }

file = open("..\input.txt", 'r')

line = file.readline()
score = 0

while(line != ""):
    actions = line.split(" ")
    opponentAction = values[actions[0].strip()]
    necessaryResult = results[actions[1].strip()]
    score = score + processScore(opponentAction, necessaryResult)
    line = file.readline()

file.close()
print(score)