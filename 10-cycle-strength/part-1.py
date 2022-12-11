cmds = [line.strip() for line in open("input.txt", "r")]

clock = 1
x = 1
signalStrength = 0
crtOutput = ""
for cmd in cmds:
    args = cmd.split(" ")

    print(f"cmd: {cmd}, clock: {clock}, x:{x}, signalStrength: {signalStrength}, clock % 40: {clock % 40}")

    if clock % 40 == 20:
        signalStrength = signalStrength + (clock * x)

    if args[0] == "noop":
        clock = clock + 1
        continue

    if clock % 40 == 19:
        print((clock+1) * x)
        signalStrength = signalStrength + ((clock+1) * x)

    x = x + int(args[1])
    clock = clock + 2

print(signalStrength)