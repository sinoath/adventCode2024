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
firstMach = listOfMachines[2]
print(listOfMachines[0])
aButton = buttonValues(firstMach[0])
bButton = buttonValues(firstMach[1])
prize = prizeCoords(firstMach[2])
print(aButton, bButton, prize)
sumX = 0
sumY = 0
results = []
for a in range(101):
    sumX = a * aButton[0]
    for b in range(101):
        sumY = b * bButton[0]
        if sumX + sumY == prize[0]:
            if (a * aButton[1] + b * bButton[1]) == prize[1]:
                results.append([a, b])

print(results)
coin_spent = []
for el in results:
    coin_spent.append(3 * el[0] + el[1])
print(coin_spent)
