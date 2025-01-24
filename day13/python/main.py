f = open("../input.txt", "r")
listOfMachines = []
indexMachine = -1
content = []
for line in f:
    content.append(line)
f.close()

clawMachine = []
for line in content:
    elem = line.strip()
    clawMachine.append(elem)
    if elem == "":
        listOfMachines.append(clawMachine)
        clawMachine = []


def buttonValues(clawMach):
    '''Return button values for a given claw machine'''
    splitted = clawMach.split(",")
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


def coinSpend(aButton, bButton, prize):
    '''Return how many times, if any, buttons have to be presed
    to reach the prize'''
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
    return results


def main():
    results = []
    for machine in listOfMachines:
        aButton = buttonValues(machine[0])
        bButton = buttonValues(machine[1])
        prize = prizeCoords(machine[2])

        results.append(coinSpend(aButton, bButton, prize))
    print(results)
    coin_spent = []
    for el in results:
        if el != []:  # not el:
            temp = []
            for combo in el:
                temp.append(combo[0] * 3 + combo[1])
            # print(el)
            coin_spent.append(min(temp))
    print(coin_spent)
    minCoinsSpent = sum(x for x in coin_spent)
    print(minCoinsSpent)


if __name__ == "__main__":
    main()
