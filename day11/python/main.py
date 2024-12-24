f = open("../test.txt", "r")
conten = []
for line in f:
    content = line.strip("\n")
f.close()

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
    pass


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
    print("test")


if __name__ == "__main__":
    main()
