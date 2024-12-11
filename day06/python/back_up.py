file = open("../test.txt", "r")
content = []
last_line_index = -1
for line in file:
    s = line.strip()
    content.append(s)
    last_line_index += 1
file.close()

pile_found = True
last_char_index = len(content[0]) - 1
for line in content:
    print(line)

print("\nLast line index : ", last_line_index)
initial_guard_pos = (-1, -1)


def change_char_at_pos(string, charPos, newChar):
    s = string[:charPos] + newChar + string[charPos+1:]
    return s


def edge_position(pos):
    if (pos[0] == 0 or pos[0] == last_line_index):
        return True
    if (pos[1] == 0 or pos[1] == last_char_index):
        return True
    return False


def find_guard(lines, char):
    l_index = -1
    for line in lines:
        l_index += 1
        if char in line:
            return (l_index, line.index(char))
    return (-1, -1)


new_content = content
initial_guard_pos = find_guard(content, "^")
x_guard = initial_guard_pos[1]
y_guard = initial_guard_pos[0]
print(initial_guard_pos)
print(f"Guard coordinates: ({x_guard}, {y_guard})")

# if edge_position(initial_guard_pos):
#     print(True)
# else:
#     print(False)

# guard moving up until Pile is found
totalGuardSteps = 0
a = 0
steps = 0
newY_guard = y_guard
for steps in range(y_guard, -1, -1):
    targetChar = content[steps][x_guard]
    if targetChar == "#":
        print("Pile found at line index: ", steps)
        print("Pile is {} lines above".format(abs(steps - y_guard)))

totalGuardSteps += (abs(steps - y_guard) - 1)
print("Total guard steps: ", totalGuardSteps)

# change the guard character according to the new coordinates
startingLine = y_guard
if steps != startingLine and steps != 0:
    newY_guard = steps+1
else:
    newY_guard = 0
new_content[startingLine] = change_char_at_pos(
    new_content[startingLine], x_guard, ".")
new_content[newY_guard] = change_char_at_pos(
    new_content[newY_guard], x_guard, "^")

for line in new_content:
    print(line)

y_guard = newY_guard

print(f"Guard coordinates: ({x_guard}, {y_guard})")

# guard moving left until Pile is found
