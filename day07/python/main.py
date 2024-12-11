import itertools

f = open("../test.txt", "r")
fileContent = []
for line in f:
    fileContent.append(line.strip())
f.close()

calibrationValues = []
for el in fileContent:
    calibrationValues.append(el.split(":"))

for value in calibrationValues:
    value[0] = int(value[0])
    value[1] = value[1].strip()
    numbers = value[1].split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    value[1] = numbers

for el in calibrationValues:
    print(el)


def mul(a, b):
    return a * b


def add(a, b):
    return a + b


def createOperators(number):
    symbols = ["*", "+"]
    operators = list(itertools.product(symbols, repeat=number))
    return operators


operatorList = createOperators(3)
print(operatorList)
