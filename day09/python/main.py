f = open("../input.txt", "r")
content = (f.readline()).strip()
f.close()

expandedString = ""
fileSystemBlocks = list()
for i in range(len(content)):
    if i % 2 == 0:
        for k in range(int(content[i])):
            fileSystemBlocks.append(i // 2)
    else:
        for k in range(int(content[i])):
            fileSystemBlocks.append(".")

compactedFileSystem = list()
for el in fileSystemBlocks:
    compactedFileSystem.append(el)

while "." in compactedFileSystem:
    element = compactedFileSystem.pop()
    index = compactedFileSystem.index(".")
    compactedFileSystem[index] = element
resultString = ""

for el in compactedFileSystem:
    resultString += str(el)

checkSum = 0
for k in range(len(compactedFileSystem)):
    checkSum += (int(compactedFileSystem[k]) * k)

print(checkSum)
