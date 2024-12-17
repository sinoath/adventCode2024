f = open("../input.txt", "r")
content = []
maxLineIndex = -1
for line in f:
    line = line.strip()
    content.append(line)
    maxLineIndex += 1
f.close()
antennasCoords = []
index_line = -1
for el in content:
    index_line += 1
    for i in range(len(el)):
        if el[i].isalnum():
            antennasCoords.append([el[i], (i, index_line)])

uniqueAntinodesCoords = set()


def inGrid(coords):
    global maxLineIndex
    global content
    xMax = len(content[0]) - 1
    yMax = maxLineIndex
    if (coords[0] < 0 or coords[0] > xMax):
        return False
    if (coords[1] < 0 or coords[1] > yMax):
        return False
    return True


def findAntinodesCoords(a, b):
    yVecDistance = b[1] - a[1]
    xVecDistance = b[0] - a[0]
    firstAntinode, secondAntinode = tuple(), tuple()
    firstAntinode = (b[0] + xVecDistance, b[1] + yVecDistance)
    secondAntinode = (a[0] - xVecDistance, a[1] - yVecDistance)
    return [firstAntinode, secondAntinode]


# Find all antinodes coordinates, check if in grid and put them in a set
for firstNode in antennasCoords:
    name = firstNode[0]
    coords1 = firstNode[1]
    for secondNode in antennasCoords:
        if secondNode != firstNode and name == secondNode[0]:
            coords2 = secondNode[1]
            temp = findAntinodesCoords(coords1, coords2)
            if inGrid(temp[0]):
                uniqueAntinodesCoords.add(temp[0])
            if inGrid(temp[1]):
                uniqueAntinodesCoords.add(temp[1])

print(len(uniqueAntinodesCoords))
