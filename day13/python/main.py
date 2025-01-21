f = open("../test.txt", "r")
listOfMachines = []
clawMachine = []
indexMachine = -1
content = []
for line in f:
    content.append(line)
f.close()

count = 0
for line in content:
    elem = line.strip()
    clawMachine.append(elem)
    if elem == "":
        listOfMachines.append(clawMachine)
        clawMachine = []


def buttonValues(clawMach):
    '''Return button values for a given claw machine'''
    splitted = clawMach.split(",")
    print(splitted)
    left = splitted[0].split("+")
    right = splitted[1].split("+")
    x = int(left[1])
    y = int(right[1])
    return [x, y]


def prizeCoords(string):
    '''Return the prize coordinates
    Input: string with the X and Y coordinates
    Output: a list with the X and Y integers'''
    splitted = string.split(",")
    left = splitted[0].split("=")
    right = splitted[1].split("=")
    x, y = int(left[1]), int(right[1])
    return [x, y]
    pass


print(listOfMachines)
print()
for el in listOfMachines:
    print(*el)
# print(clawMachines[0])
