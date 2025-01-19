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


print(listOfMachines)
print()
for el in listOfMachines:
    print(*el)
# print(clawMachines[0])
