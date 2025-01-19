import re

f = open("../test.txt", "r")
content = []
lineMaxIndex = -1
for line in f:
    line = line.strip("\n")
    content.append(line)
    lineMaxIndex += 1
f.close()
stringMaxIndex = len(content[0]) - 1


def inGrid(coords):
    '''Check if a pair of coordinates are inside or outside a grid.
    Return a boolean'''
    x = coords[0]
    if x < 0 or x > stringMaxIndex:
        return False
    y = coords[1]
    if y < 0 or y > lineMaxIndex:
        return False
    return True


def wholeprint(mylist: list):
    '''Just print line by line a list'''
    for el in mylist:
        print(el)


def trailStartCoords(grid: list, target):
    '''Return a list of starting point coordinates, given a list
    of lines representing the grid'''
    y = -1
    coords = []
    for line in grid:
        y += 1
        xPositions = [i.start() for i in re.finditer(target, line)]
        coords.append(xPositions)
    return coords


def nextHikingTrails(coords):
    '''Return the coordinates of the next step of the hiking trail,
    if the next step exist. Return [-1, -1] otherwise'''
    global content
    # result = []
    charID, y = coords[0], coords[0]  # this is Y as coordinate
    lineID, x = coords[1], coords[1]  # this is X as coordinate
    value = int(content[lineID][charID])
    # nextStep = chr(value + 1)
    up = [x, y - 1]
    right = [x + 1, y]
    down = [x, y + 1]
    left = [x - 1, y]

    if inGrid(up) and content:
        pass

    if inGrid(down) and content:
        pass

    if inGrid(left) and content:
        pass

    if inGrid(right) and content:
        pass

    pass


def main():
    wholeprint(content)
    trailHeads = trailStartCoords(content, "0")
    print()
    print(trailHeads)
    # wholeprint(content)
    print(*content[0])


if __name__ == "__main__":
    main()
