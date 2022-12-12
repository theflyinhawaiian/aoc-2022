cmds = [line.strip() for line in open("input.txt", "r")]

clock = 1
x = 1
crtOutput = ""
currCmd = 0
processing = False
while currCmd < len(cmds):
    args = cmds[currCmd].split(" ")
    if not processing:
        if args[0] == "addx":
            processing = True
    else:
        processing = False

    if not processing:
        if args[0] == "addx":
            x = x + int(args[1])
        
        currCmd = currCmd + 1
        
    if abs((clock % 40) - x) <= 1:
        char = "#" 
    else:
        char = "."
    crtOutput = crtOutput + char

    if clock % 40 == 39:
        crtOutput = crtOutput + "\n"
    
    clock = clock + 1

print(f"{crtOutput}")