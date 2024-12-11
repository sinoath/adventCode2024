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


# def change_char_at_pos(string, charPos, newChar):
#     s = string[:charPos] + newChar + string[charPos+1:]
#     return s

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


def matrixCharChange(listOfStrings, char, position):
    pass


def find_guard(lines, char):
    l_index = -1
    for line in lines:
        l_index += 1
        if char in line:
            return (l_index, line.index(char))
    return (-1, -1)


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
x_guard = initial_guard_pos[1]
y_guard = initial_guard_pos[0]
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
        result = edge
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

    # uniqueSteps.remove(old_guard_pos)
    if found == edge:
        result = (last_char_index, y_guard)
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
    else:
        result = (found[0] + 1, y_guard)
    return result


# going up ----------------------------
tempPosition = move_up(old_guard_pos)
if tempPosition != (-1, -1):
    new_guard_pos = tempPosition
    x_guard, y_guard = new_guard_pos[0], new_guard_pos[1]
print(f"Actual guard coordinates: ({x_guard}, {y_guard})")
change_guard_pos(old_guard_pos, new_guard_pos)

# print matrix after moving up
for line in new_content:
    print(line)

old_guard_pos = new_guard_pos

# going right ---------------------
tempPosition = move_right(old_guard_pos)
if tempPosition != (-1, -1):
    new_guard_pos = tempPosition
    x_guard, y_guard = new_guard_pos[0], new_guard_pos[1]
print(f"Actual guard coordinates: ({x_guard}, {y_guard})")
change_guard_pos(old_guard_pos, new_guard_pos)

# print matrix after moving right
for line in new_content:
    print(line)

old_guard_pos = new_guard_pos


# going down ---------------------
tempPosition = move_down(old_guard_pos)
if tempPosition != (-1, -1):
    new_guard_pos = tempPosition
    x_guard, y_guard = new_guard_pos[0], new_guard_pos[1]
print(f"Actual guard coordinates: ({x_guard}, {y_guard})")
change_guard_pos(old_guard_pos, new_guard_pos)

# print matrix after moving down
for line in new_content:
    print(line)

old_guard_pos = new_guard_pos


# going left -----------------------
tempPosition = move_left(old_guard_pos)
if tempPosition != (-1, -1):
    new_guard_pos = tempPosition
    x_guard, y_guard = new_guard_pos[0], new_guard_pos[1]
print(f"Actual guard coordinates: ({x_guard}, {y_guard})")
change_guard_pos(old_guard_pos, new_guard_pos)

old_guard_pos = new_guard_pos

# print matrix after moving left
for line in new_content:
    print(line)

# print("\nUnique steps after moving up: ", up)
# print("Number of elements in the set above: ", len(list(up)))
print("\nUnique steps after moving down: ", uniqueSteps)
print("Number of elements in the set above: ", len(list(uniqueSteps)))

for pos in uniqueSteps:
    new_content[pos[1]] = changeCharAtPos("X", new_content[pos[1]], pos)

for line in new_content:
    print(line)
