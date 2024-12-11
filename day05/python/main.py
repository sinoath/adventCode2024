rulesFile = open("../rules.txt", "r")
dataFile = open("../data.txt", "r")

rulesList = []
dataList = []
for line in rulesFile:
    clean = line.strip()
    element = clean.split("|")
    rulesList.append(element)

for line in dataFile:
    clean = line.strip()
    element = clean.split(",")
    dataList.append(element)

    # for i in range(0, len(element)):
    #     element[i] = int(element[i])
dataFile.close()
# print(rulesList)

unordered = []
for data in dataList:
    for rule in rulesList:
        if rule[0] in data and rule[1] in data:
            if data.index(rule[0]) > data.index(rule[1]):
                unordered.append(data)
                break

# print(unordered)
# print((rulesList[0][0] in dataList[0] and rulesList[0][1] in dataList[0]))
# print(dataList[0].index(rulesList[0][0]))
# print(dataList[0].index(rulesList[0][1]))
print(unordered)
following_rules = dataList
for el in unordered:
    following_rules.remove(el)

print(following_rules)

result = 0
for el in following_rules:
    result += int(el[len(el)//2])

print("Sum: ", result)
