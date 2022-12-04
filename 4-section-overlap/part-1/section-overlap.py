groupings = [line.strip() for line in open("..\input.txt", "r")]

numContainments = 0

for grouping in groupings:
    sections = grouping.split(",")
    sets = []
    for section in sections:
        bounds = [int(num) for num in section.split("-")]
        sets.append(set(range(bounds[0], bounds[1]+1)))
    
    intersection = sets[0].intersection(sets[1])
    if(intersection == sets[0] or intersection == sets[1]):
        numContainments = numContainments + 1

print(numContainments)