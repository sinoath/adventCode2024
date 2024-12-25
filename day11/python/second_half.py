f = open("../test.txt", "r")
conten = []
for line in f:
    content = line.strip("\n")
f.close()

NUMBER_OF_BLINKS = 25
LARGER_NUM_OF_BLINKS = 75
stones = content.split(" ")
dictStones = {key: 1 for key in stones}


def mySplit(char):
    lenght = len(char)
    firstStone = char[:(lenght // 2)]
    tempStone = char[(lenght // 2):]
    while tempStone[0] == "0":
        if len(tempStone) > 1:
            tempStone = tempStone[1:]
        else:
            break
    return [firstStone, tempStone]


def insertSplitStone(stones, myDict):
    for elem in stones:
        if elem in myDict.keys():
            myDict[elem] += myDict[elem]
        else:
            myDict[elem] = 1


def insertStone(stone, myDict, value=1):
    if stone in myDict.keys():
        myDict[stone] += value
        # myDict[stone] += myDict[stone]
    else:
        myDict[stone] = value


def multi2024(char):
    i = int(char)
    i *= 2024
    return str(i)


# testChar = "1013102030"
# result = mySplit(testChar)

# randomList = [str(i) for i in range(6)]
# print(randomList)
# index = 2
# # randomList[index] = result[1]
# # randomList.insert(index, result[0])
# insertSplitStone(index, randomList, result)
# print(randomList)
# print(multi2024("2"))
# # print(testChar)
# # print(result)


def main():

    BLINKS = 6
    # cycle = 1
    for _ in range(BLINKS):

        toBeSplit = []
        toBeMulti = []
        for k, v in dictStones.items():
            if (len(k) % 2) == 0:
                occurencies = dictStones[k]
                toBeSplit.append([k, occurencies])
                # temp = mySplit(k)
                # insertStone(temp, dictStones)
            elif k != "0":
                toBeMulti.append(k)
                # new_k = multi2024(k)
                # print(new_k)
                # dictStones[multi2024(k)] = dictStones[k]
                # del dictStones[k]

        if "0" in dictStones.keys():
            dictStones["1"] = dictStones["0"]
            del dictStones["0"]

        tempDict = dict()
        for key in toBeMulti:
            new_key = multi2024(key)
            tempDict[new_key] = dictStones[key]
            del dictStones[key]

        for element in toBeSplit:
            value = element[1]
            key = element[0]
            # print("Key and value in split: ", key, value)
            temp = mySplit(key)
            dictStones.pop(key)
            insertStone(temp[0], dictStones, value)
            insertStone(temp[1], dictStones, value)
            for k, v in tempDict.items():
                dictStones[k] = v
            # dictStones[temp[0]] = value
            # dictStones[temp[1]] = value

        # print()
        # print("After ", cycle, " blinks")
        # for k, v in dictStones.items():
        #     print(k, " ", v)
        # cycle += 1
        # print(dictStones)

    numberOfStones = 0
    for el in dictStones:
        numberOfStones += dictStones[el]
    print(numberOfStones)


if __name__ == "__main__":
    main()
