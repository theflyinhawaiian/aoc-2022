def findCommonChar(str):
    index1 = 0
    index2 = len(str)//2

    list1 = []
    list2 = []

    for i in range(0, len(str)//2):
        char1 = str[index1 + i]
        char2 = str[index2 + i]
        if char1 not in list1:
            if char1 in list2:
                return char1
            else:
                list1.append(char1)
        
        if char2 not in list2:
            if char2 in list1:
                return char2
            else:
                list2.append(char2)

def getValue(char):
    if(ord(char) - 96 < 0):
        return ord(char) - 64 + 26
    else:
        return ord(char) - 96

file = open("..\input.txt","r")

input = file.readline()
sum = 0

while input != "":
    sum = sum + getValue(findCommonChar(input.strip()))
    input = file.readline()

print(sum)

file.close()