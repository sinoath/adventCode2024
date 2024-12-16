f = open("../test.txt", "r")
content = []
for line in f:
    line = line.strip()
    content.append(line)
f.close()
antennasCoords = []
index_line = -1
for el in content:
    index_line += 1
    for i in range(len(el)):
        if el[i].isalnum():
            antennasCoords.append([el[i], (i, index_line)])

for line in antennasCoords:
    print(line)
