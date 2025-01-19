f = open("../test.txt", "r")
content = (f.readline()).strip()
f.close()

# content = "2333133121414131499"
blocksOfFileSystem = list()
for i in range(len(content)):
    fileLenght = int(content[i])
    if i % 2 == 0:
        for k in range(fileLenght):
            blocksOfFileSystem.append([i // 2, fileLenght])
    else:
        for k in range(fileLenght):
            blocksOfFileSystem.append([".", fileLenght])

# print(fileSystemBlocks)
fileSystem = list()
for el in blocksOfFileSystem:
    fileSystem.append(el)


# Function for test only
def strFileSystem(fileSys):
    '''Print a string representing file system, where dots are free space
    and numbers are file blocks'''
    resultString = ""
    for el in fileSys:
        resultString += str(el[0])
    # print(resultString)
    return resultString


def moveFile(file, position):
    '''Move the file in the position specified, change the old file position as
    a free space representation (dots), update the dimension
    of free space blocks accordingly'''
    global fileSystem
    firstEmptyBlock = fileSystem[position]
    emptyBlockDimension = firstEmptyBlock[1]
    fileName = file[0]
    fileDimension = file[1]
    filePosition = fileSystem.index([fileName, fileDimension])
    updatedEmptyBlockDimension = emptyBlockDimension - fileDimension
    for k in range(emptyBlockDimension):
        fileSystem[position + k][1] = updatedEmptyBlockDimension
    for k in range(fileDimension):
        fileSystem[filePosition + k][0] = "."
        fileSystem[(position + k)][0] = fileName


def findEnoughSpace(file):
    '''Return the block position with enough free space to contain a file.
    Input is a list, with fileName and fileDimension in it'''
    global fileSystem
    position = -1
    # fileName = file[0]
    fileDimension = file[1]
    # filePosition = compactedFileSystem.index([fileName, fileDimension])
    for el in fileSystem:
        elName, elDimension = el[0], el[1]
        if elName == "." and elDimension >= fileDimension:
            position = fileSystem.index(el)
            break
    return position


# this function is just for test
def indexFromValue(value: int):
    '''Given a value (fileName), return the first block position of the file'''
    global fileSystem
    for file in fileSystem:
        if file[0] == value:
            return fileSystem.index(file)
    return -1


def rightmostFileValue():
    '''Return the rightmost not empty block name'''
    global fileSystem
    for k in range(len(fileSystem) - 1, 0, -1):
        value = fileSystem[k][0]
        if value != ".":
            return value
    return -1


strFS = strFileSystem(fileSystem)
print(strFS)

startingValue = rightmostFileValue()
while startingValue > 0:
    filePos = indexFromValue(startingValue)
    tempFile = fileSystem[filePos]
    emptyPos = findEnoughSpace(tempFile)
    if emptyPos > -1 and emptyPos < filePos:
        moveFile(tempFile, emptyPos)
    strFileSystem(fileSystem)
    startingValue -= 1
# for k in range(len(fileSystem) - 1, 0, - 1):
strFileSystem(fileSystem)

strFS = strFileSystem(fileSystem)
print(strFS)

checkSum = 0
for k in range(len(strFS)):
    block = strFS[k]
    if block == ".":
        pass
    else:
        checkSum += (int(block) * k)

print(checkSum)
