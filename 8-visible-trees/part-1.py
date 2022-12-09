trees = [line.strip() for line in open("input.txt", "r")]

visibleTrees = []

for i in range(len(trees)):
    tallestVisibleTree = -1
    for j in range(len(trees[i])):
        tree = int(trees[i][j])
        if(tallestVisibleTree < tree):
            tallestVisibleTree = tree
            if (i,j) not in visibleTrees:
                visibleTrees.append((i, j))
                print(f"{i}, {j}")
        
        if(tree == 9):
            break

for i in range(len(trees)-1, -1, -1):
    tallestVisibleTree = -1
    for j in range(len(trees[i])-1, -1, -1):
        tree = int(trees[i][j])
        if(tallestVisibleTree < tree):
            tallestVisibleTree = tree
            if (i,j) not in visibleTrees:
                visibleTrees.append((i, j))
                print(f"{i}, {j}")
        
        if(tree == 9):
            break

for i in range(len(trees)):
    tallestVisibleTree = -1
    for j in range(len(trees[i])):
        tree = int(trees[j][i])
        if(tallestVisibleTree < tree):
            tallestVisibleTree = tree
            if (j,i) not in visibleTrees:
                visibleTrees.append((j, i))
                print(f"{j}, {i}")
        
        if(tree == 9):
            break

for i in range(len(trees)-1, -1, -1):
    tallestVisibleTree = -1
    for j in range(len(trees[i])-1, -1, -1):
        tree = int(trees[j][i])
        if(tallestVisibleTree < tree):
            tallestVisibleTree = tree
            if (j,i) not in visibleTrees:
                visibleTrees.append((j,i))
                print(f"{j}, {i}")
        
        if(tree == 9):
            break

print(f"There are {len(visibleTrees)} visible trees.")