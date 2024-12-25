f = open("../input.txt", "r")
conten = []
for line in f:
    content = line.strip("\n")
f.close()

NUMBER_OF_BLINKS = 25
LARGER_NUM_OF_BLINKS = 75
# stones = content.split(" ")
# dictStones = {key: 1 for key in stones}
# print(dictStones)


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


def main():

    BLINKS = 101
    # cycle = 1
    stones = content.split(" ")
    dictStones = {key: 1 for key in stones}
    # print(dictStones)
    for _ in range(BLINKS):

        toBeSplit = dict()
        toBeMulti = dict()
        zeroToOne = dict()
        for k, v in dictStones.items():
            # if (len(k) % 2) == 0:
            #     toBeSplit[k] = v
            if k == "0":
                zeroToOne[k] = v
            elif (len(k) % 2) == 0:
                toBeSplit[k] = v
            else:
                toBeMulti[k] = v

        dictStones = dict()
        # print("Split: ", toBeSplit)
        # print("Multi: ", toBeMulti)
        # print("Zeros: ", zeroToOne)

        # Adding stones with inscription 0
        if zeroToOne != {}:
            dictStones["1"] = zeroToOne["0"]

        # Adding stones with splitted incriptions
        for key, value in toBeSplit.items():
            stones = mySplit(key)
            insertStone(stones[0], dictStones, value)
            insertStone(stones[1], dictStones, value)
            # dictStones[stones[0]] = value
            # dictStones[stones[1]] = value

        # Adding stones with multiplied inscription
        for key, value in toBeMulti.items():
            new_key = multi2024(key)
            dictStones[new_key] = value

        # ones = 0
        # if "1" in dictStones.keys():
        #     ones += dictStones["1"]
        # if zeroToOne != {}:
        #     ones += zeroToOne["0"]
        # if ones > 0:
        #     dictStones["1"] = ones

        # print()
        # print("After ", cycle, " blinks")
        # for k, v in dictStones.items():
        #     print(k, " ", v)
        # cycle += 1
        # print("After ", cycle, " blinks")
        # print(dictStones)
        # print()
        # cycle += 1

    numberOfStones = 0
    for el in dictStones:
        numberOfStones += dictStones[el]
    print(numberOfStones)
    # after 25 cycles the answer is correct 193899
    # after 75 cycles, 229682156298283 is not the correct answer


if __name__ == "__main__":
    main()
