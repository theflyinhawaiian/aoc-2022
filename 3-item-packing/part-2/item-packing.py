def getValue(char):
    if(ord(char) - 96 < 0):
        return ord(char) - 64 + 26
    else:
        return ord(char) - 96

def parseRucksacks(packs):
    idx = 0
    contents = [[], [], []]

    while idx < len(packs[2]):
        packIdx = 0
        while packIdx < len(packs):
            if(len(packs[packIdx]) <= idx):
                packIdx = packIdx + 1
                continue

            matchCount = 0
            char = packs[packIdx][idx]

            dictIdx = 0
            while dictIdx < len(contents):
                if char in contents[dictIdx] and dictIdx != packIdx:
                    matchCount = matchCount + 1
                dictIdx = dictIdx + 1
            
            if matchCount == 2:
                return char
            else:
                contents[packIdx].append(char)

            
            packIdx = packIdx + 1
        idx = idx + 1


file = open("..\input.txt","r")

text = "hi"
sum = 0

while text != "":
    elves = []
    for i in range(3):
        text = file.readline().strip()
        if text == "":
            print(sum)
            exit()
        elves.append(text)
    
    elves.sort(key = lambda x: len(x))
    
    commonChar = parseRucksacks(elves)

    sum = sum + getValue(commonChar)


file.close()