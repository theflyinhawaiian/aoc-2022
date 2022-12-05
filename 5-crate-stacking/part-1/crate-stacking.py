# [C]         [S] [H]                
# [F] [B]     [C] [S]     [W]        
# [B] [W]     [W] [M] [S] [B]        
# [L] [H] [G] [L] [P] [F] [Q]        
# [D] [P] [J] [F] [T] [G] [M] [T]    
# [P] [G] [B] [N] [L] [W] [P] [W] [R]
# [Z] [V] [W] [J] [J] [C] [T] [S] [C]
# [S] [N] [F] [G] [W] [B] [H] [F] [N]
#  1   2   3   4   5   6   7   8   9 


stacks = [
    ["S", "Z", "P", "D", "L", "B", "F", "C"], 
    ["N", "V", "G", "P", "H", "W", "B"], 
    ["F", "W", "B", "J", "G"], 
    ["G", "J", "N", "F", "L", "W", "C", "S"], 
    ["W", "J", "L", "T", "P", "M", "S", "H"], 
    ["B", "C", "W", "G", "F", "S"], 
    ["H","T","P","M","Q","B","W"], 
    ["F","S","W","T"], 
    ["N","C","R"]
]

commands = [line.strip() for line in open("..\input.txt", "r")]

for command in commands:
    args = [int(el) for el in command.split(" ")]
    for i in range(args[0]):
        crate = stacks[args[1]-1].pop()
        stacks[args[2]-1].append(crate)

output = ""
for stack in stacks:
    output = output + stack.pop()

print(output)