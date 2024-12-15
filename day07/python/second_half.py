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
    '''Based on the sign, return addition or multiplication result between
    a and b'''
    if sign == "+":
        return a + b
    else:
        return a * b


def createOperators(number):
    '''Return a list of all combination between symbols "+" and "*", repeated
    "number" times'''
    symbols = ["*", "+"]
    operators = list(itertools.product(symbols, repeat=number))
    return operators


def combineNumbers(a, b):
    '''Combine "a" and "b" into a single number "ab"'''
    x = str(a)
    y = str(b)
    combo = (x + y)
    result = int(combo)
    return result


fullOperatorList = []
for line in calibrationValues:
    number = len(line[1]) - 1
    fullOperatorList.append(createOperators(number))


def checkCalibration(target, values, operators):
    '''Check if the combinations of mul and add of values produces a result
    equal to target. Return a boolean'''
    for el in operators:
        result = values[0]
        for i in range(len(el)):
            result = signedOperation(result, values[i+1], el[i])
            if result == target:
                return True
    return False


def adjacentCoupleList(values: list):
    '''Given a list of number (values) return a list of the adjacent couples
    combined together (15 and 21 combined is 1521). The combined numbers are
    the first and the second, then the second and the third and so on'''
    maxIndex = len(values) - 1
    tempList = []
    numbers = values
    cycle = 1
    while cycle <= maxIndex:
        tempList.append(combineNumbers(numbers[cycle - 1], numbers[cycle]))
        cycle += 1
    return tempList


def concatenatedList(comboedData, dataList):
    '''Return a list where the combined data "x" in comboedData take place of
    the couple of data "a" and "b" that compose "x" through combineNumbers(),
    The returned list, is a list of lists where "x" is the first, second,
    third (and so on) element'''
    lastIndex = len(comboedData) - 1
    result = []
    cycle = 0
    while cycle <= lastIndex:
        temp = []
        for i in range(len(dataList)):
            if i == cycle:
                temp.insert(i, listOp[i])
                j = i + 2
                while j <= (len(dataList) - 1):
                    temp.insert(j, dataList[j])
                    j += 1
                break
            temp.insert(i, dataList[i])
            print("inside func: i = {} temp = {}".format(i, temp))
        result.append(temp)
        cycle += 1
    return result


def valuePassCheck(values, operators):
    result = []
    for val, op in zip(values, operators):
        target = val[0]
        values = val[1]
        if checkCalibration(target, values, op):
            result.append(val)
    return result


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
uniqueValidCalibrations = set(validCalibrationValues)
for el in uniqueValidCalibrations:
    print(el)

