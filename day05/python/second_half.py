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

following_rules = dataList
for el in unordered:
    following_rules.remove(el)

result = 0
for el in following_rules:
    result += int(el[len(el)//2])

print("Sum: ", result)


def switchListElements(a, b, mylist):
    index_a = mylist.index(a)
    index_b = mylist.index(b)
    mylist[index_a] = b
    mylist[index_b] = a


# switchListElements(1, 3, test)
# print(test)

# orderedData = []
repeat_flag = False

for test in unordered:
    for rule in rulesList:
        if rule[0] in test and rule[1] in test:
            if test.index(rule[0]) > test.index(rule[1]):
                switchListElements(rule[0], rule[1], test)
                repeat_flag = True

    while repeat_flag:
        repeat_flag = False
        for rule in rulesList:
            if rule[0] in test and rule[1] in test:
                if test.index(rule[0]) > test.index(rule[1]):
                    switchListElements(rule[0], rule[1], test)
                    repeat_flag = True


result = 0
for el in unordered:
    result += int(el[len(el)//2])
print(result)
