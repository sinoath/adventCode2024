import itertools

f = open("../test.txt", "r")
fileContent = []
for line in f:
    fileContent.append(line.strip())
f.close()

validCalibrationValues = []
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


def signedOperation(a, b, sign):
    if sign == "+":
        return a + b
    else:
        return a * b


def createOperators(number):
    symbols = ["*", "+"]
    operators = list(itertools.product(symbols, repeat=number))
    return operators


fullOperatorList = []
for line in calibrationValues:
    number = len(line[1]) - 1
    fullOperatorList.append(createOperators(number))


def checkCalibration(target, values, operators):
    for el in operators:
        result = values[0]
        for i in range(len(el)):
            result = signedOperation(result, values[i+1], el[i])
            if result == target:
                return True
    return False


for val, op in zip(calibrationValues, fullOperatorList):
    target = val[0]
    values = val[1]
    if checkCalibration(target, values, op):
        validCalibrationValues.append(val)
print(validCalibrationValues)
finalValue = 0
for el in validCalibrationValues:
    finalValue += el[0]
print(finalValue)

discardedValues = []
for el in calibrationValues:
    if el in validCalibrationValues:
        pass
    else:
        discardedValues.append(el)
