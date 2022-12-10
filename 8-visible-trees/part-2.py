def visibleTreesNorth(x, startY):
    height = int(trees[startY][x])
    numVisible = 0
    for i in range(startY-1, -1, -1):
        tree = int(trees[i][x])
        if i != startY and tree >= height:
            return numVisible + 1
        else:
            numVisible = numVisible + 1

    return numVisible

def visibleTreesSouth(x, startY):
    height = int(trees[startY][x])
    numVisible = 0
    for i in range(startY+1, len(trees)):
        tree = int(trees[i][x])
        if i != startY and tree >= height:
            return numVisible + 1
        else:
            numVisible = numVisible + 1

    return numVisible
    
def visibleTreesWest(startX, y):
    height = int(trees[y][startX])
    #print(height)
    numVisible = 0
    for i in range(startX-1, -1, -1):
        tree = int(trees[y][i])
        #print(tree)
        if i != startX and tree >= height:
            return numVisible + 1
        else:
            numVisible = numVisible + 1

    return numVisible
    
def visibleTreesEast(startX, y):
    height = int(trees[y][startX])
    numVisible = 0
    for i in range(startX+1, len(trees[y])):
        tree = int(trees[y][i])
        if tree >= height:
            return numVisible + 1
        else:
            numVisible = numVisible + 1

    return numVisible

trees = [line.strip() for line in open("input.txt", "r")]

highScore = 0
for i in range(len(trees)):
    for j in range(len(trees[i])):
        treesNorth = visibleTreesNorth(i, j)
        treesSouth = visibleTreesSouth(i, j)
        treesWest = visibleTreesWest(i, j)
        treesEast = visibleTreesEast(i, j)

        product = treesNorth * treesSouth * treesEast * treesWest

        if product > highScore:
            highScore = product

print(highScore)