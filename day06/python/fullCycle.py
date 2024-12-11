import re

file = open("../test.txt", "r")
content = []
last_line_index = -1
for line in file:
    s = line.strip()
    content.append(s)
    last_line_index += 1
file.close()

total_steps = 0
uniqueSteps = set()
last_char_index = len(content[0]) - 1

# print("\nLast line index : ", last_line_index)
initial_guard_pos = (-1, -1)
new_content = content
originalMatrixDimension = ()


def countChar(char, listChar):
    counter = 0
    for line in listChar:
        temp = [i.start() for i in re.finditer(char, line)]
        counter += len(temp)
    return counter


def change_guard_pos(old_pos, new_pos):
    global new_content
    s1 = new_content[old_pos[1]]
    new_content[old_pos[1]] = changeCharAtPos(".", s1, old_pos)
    s2 = new_content[new_pos[1]]
    new_content[new_pos[1]] = changeCharAtPos("^", s2, new_pos)


def changeCharAtPos(newChar, mystring, pos):
    # global new_content
    mystring = mystring[:pos[0]] + newChar + mystring[pos[0] + 1:]
    return mystring


def find_guard(lines, char):
    l_index = -1
    for line in lines:
        l_index += 1
        if char in line:
            x = line.index(char)
            return (x, l_index)
    return (-1, -1)


def isEdge(position):
    if position[0] == 0 or position[0] == last_char_index:
        return True
    elif position[1] == 0 or position[1] == last_line_index:
        return True
    return False


def find_blocks_coords(lines, char):
    y = -1
    blocks = []
    for line in lines:
        y += 1
        x_pos = [i.start() for i in re.finditer(char, line)]
        for x in x_pos:
            blocks.append((x, y))
        # blocks.append
    return blocks


counterUniqueSteps = 0
new_content = content
blocks_pos = find_blocks_coords(content, "#")
initial_guard_pos = find_guard(content, "^")
x_guard = initial_guard_pos[0]
y_guard = initial_guard_pos[1]
old_guard_pos = (x_guard, y_guard)
startinPos = old_guard_pos
new_guard_pos = ()

print(f"Actual guard coordinates: ({x_guard}, {y_guard})")
for line in content:
    print(line)

# print(blocks_pos)


# move up guards #######################
def move_up(startingPosition):
    found = (-1, -1)
    edge = found
    x_guard, y_guard = startingPosition[0], startingPosition[1]
    for i in range(y_guard - 1, -1, -1):
        if (x_guard, i) in blocks_pos:
            found = (x_guard, i)
            break
        else:
            uniqueSteps.add((x_guard, i))

    if found == edge:
        result = (x_guard, 0)
        uniqueSteps.add(result)
    else:
        result = (found[0], found[1] + 1)
    return result


# move guard right ###################################
def move_right(startPosition):
    x_guard, y_guard = startPosition[0], startPosition[1]
    found = (-1, -1)
    edge = found
    for i in range(x_guard + 1, last_char_index + 1):
        if (i, y_guard) in blocks_pos:
            found = (i, y_guard)
            break
        else:
            uniqueSteps.add((i, y_guard))

    if found == edge:
        result = (last_char_index, y_guard)
        uniqueSteps.add(result)
    else:
        result = (found[0] - 1, y_guard)
    return result


# move guard down
def move_down(startPosition):
    x_guard, y_guard = startPosition[0], startPosition[1]
    found = (-1, -1)
    edge = found
    for i in range(y_guard + 1, last_line_index + 1):
        if (x_guard, i) in blocks_pos:
            found = (x_guard, i)
            break
        else:
            uniqueSteps.add((x_guard, i))

    if found == edge:
        result = (x_guard, last_line_index)
        uniqueSteps.add(result)
    else:
        result = (x_guard, found[1] - 1)
    return result


# move guard left #####################################
def move_left(startPosition):
    x_guard, y_guard = startPosition[0], startPosition[1]
    found = (-1, -1)
    edge = found
    for i in range(x_guard - 1, -1, -1):
        if (i, y_guard) in blocks_pos:
            found = (i, y_guard)
            break
        else:
            uniqueSteps.add((i, y_guard))

    if found == edge:
        result = (0, y_guard)
        uniqueSteps.add(result)
    else:
        result = (found[0] + 1, y_guard)
    return result


circles = 0
# starting full cycle here
while old_guard_pos != (-1, -1):
    # going up ----------------------------
    tempPosition = move_up(old_guard_pos)
    if isEdge(tempPosition) or tempPosition == (-1, -1):
        break
    else:
        new_guard_pos = tempPosition
        x_guard, y_guard = new_guard_pos[0], new_guard_pos[1]

    old_guard_pos = new_guard_pos

    tempPosition = move_right(old_guard_pos)
    if isEdge(tempPosition) or tempPosition == (-1, -1):
        break
    else:
        new_guard_pos = tempPosition
        x_guard, y_guard = new_guard_pos[0], new_guard_pos[1]

    old_guard_pos = new_guard_pos

    # going down ---------------------
    tempPosition = move_down(old_guard_pos)
    if isEdge(tempPosition) or tempPosition == (-1, -1):
        break
    else:
        new_guard_pos = tempPosition
        x_guard, y_guard = new_guard_pos[0], new_guard_pos[1]

    old_guard_pos = new_guard_pos

    # going left -----------------------
    tempPosition = move_left(old_guard_pos)
    if isEdge(tempPosition) or tempPosition == (-1, -1):
        break
    else:
        new_guard_pos = tempPosition
        x_guard, y_guard = new_guard_pos[0], new_guard_pos[1]

    old_guard_pos = new_guard_pos
    # circles += 1


print("Above is the input matrix\n")

for pos in uniqueSteps:
    new_content[pos[1]] = changeCharAtPos("X", new_content[pos[1]], pos)

newContentLineMaxIndex = -1
for line in new_content:
    newContentLineMaxIndex += 1
    print(line)
newContentCharMaxIndex = len(new_content[7]) - 1
newContentDimension = (newContentCharMaxIndex, newContentLineMaxIndex)
print("Number of unique steps: ", len(list(uniqueSteps)))
print("Unique steps list: ", uniqueSteps)
print("(4, 0) in list: ", ((4, 0) in uniqueSteps))
print("Initial position {} in list: ".format(
    initial_guard_pos), ((4, 0) in uniqueSteps))
print("Number of X character in the matrix: ", countChar("X", new_content))

# print(type(re.findall("X", new_content[1])))
# print(circles)
# print("Old content dimension: ", (last_char_index, last_line_index))
# print("New content dimension: ", newContentDimension)
#
# file = open("../input.txt", "r")
# content = []
# last_line_index = -1
# for line in file:
#     s = line.strip()
#     content.append(s)
#     last_line_index += 1
# file.close()
#
# print(content[45])
# print(content[45].index("^"))
