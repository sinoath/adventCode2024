f = open("../test.txt", "r")
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

for line in antennasCoords:
    print(line)


def inGrid(coords):
    global maxLineIndex
    global content
    xMax = len(content[0])
    yMax = maxLineIndex
    if (coords[0] < 0 or coords[0] > xMax):
        return False
    if (coords[1] < 0 or coords[1] > yMax):
        return False
    return True


def findAntinodesCoords(a, b):
    yVecDistance = b[1] - a[1]
    xVecDistance = b[0] - a[0]
    firstAntinode, secondAntinode = set(), set()
    firstAntinode = (b[0] + xVecDistance, b[1] + yVecDistance)
    secondAntinode = (a[0] - xVecDistance, a[1] - yVecDistance)
    # if xVecDistance < 0:
    #     firstAntinode = (b[0] + xVecDistance, b[1] + yVecDistance)
    # else:
    #     firstAntinode = (b[0] - xVecDistance, b[1] + yVecDistance)
    # if xVecDistance > 0:
    #     firstAntinode = (b[0] - xVecDistance, b[1] - yVecDistance)
    # else:
    #     firstAntinode = (b[0] + xVecDistance, b[1] - yVecDistance)
    return [firstAntinode, secondAntinode]


print("In grid antenna: ", inGrid(antennasCoords[3][1]))
print("In grid antenna: ", inGrid((16, 9)))
result = findAntinodesCoords(antennasCoords[0][1], antennasCoords[1][1])
print(result)
