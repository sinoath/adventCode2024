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


def wholeprint(mylist: list):
    for el in mylist:
        print(el)


def trailStartCoords(grid: list, target):
    y = -1
    coords = []
    for line in grid:
        y += 1
        xPositions = [i.start() for i in re.finditer(target, line)]
        coords.append(xPositions)
    return coords


def main():
    trailHeads = trailStartCoords(content, "0")
    print(trailHeads)
    # wholeprint(content)
    print(*content[0])


if __name__ == "__main__":
    main()
