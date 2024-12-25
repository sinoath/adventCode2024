f = open("../input.txt", "r")
conten = []
for line in f:
    content = line.strip("\n")
f.close()

NUMBER_OF_BLINKS = 25
LARGER_NUM_OF_BLINKS = 75
stones = content.split(" ")


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


def insertSplitStone(index, stones, splittedStones):
    stones[index] = splittedStones[1]
    stones.insert(index, splittedStones[0])


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
    # print(stones)
    # print(len(stones[0]))
    # print(len(stones[1]))
    # print(len(stones[1]) // 2)
    # print(2 % 2)
    # for i in range(LARGER_NUM_OF_BLINKS):
    for i in range(NUMBER_OF_BLINKS):

        toBeSplitIndex = []
        for i in range(len(stones)):
            if stones[i] == "0":
                stones[i] = "1"
            elif (len(stones[i]) % 2) == 0:
                # print(stones[i])
                toBeSplitIndex.insert(0, i)
                # temp = mySplit(stones[i])
                # insertSplitStone(i, stones, temp)
            else:
                stones[i] = multi2024(stones[i])
        for k in toBeSplitIndex:
            temp = mySplit(stones[k])
            insertSplitStone(k, stones, temp)

    # print(toBeSplitIndex)
    print(stones)
    print(len(stones))


if __name__ == "__main__":
    main()
