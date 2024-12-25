randomList = [str(i) for i in range(6)]
print(randomList)
myDict = dict()
for el in randomList:
    myDict[el] = 1
print(myDict)
test = "5"
if test in myDict.keys():
    myDict[test] += myDict[test]
else:
    myDict[test] = 1

print(myDict)
for el in myDict:
    print(el)
