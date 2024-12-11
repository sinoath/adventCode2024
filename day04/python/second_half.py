import re

file = open("../input.txt", "r")
rows = []
total_pattern_found = 0
line_index = -1

for line in file:
    rows.append(line)
    line_index += 1
file.close()
pattern = "MAS"

# Find all first letter occurencies for 'pattern' (XMAS)
all_found_locations = []
full_line_found = ()
for k in range(1, len(rows) - 1):
    found_in_line = []
    search_target = rows[k]
    for i in re.finditer(pattern[1], search_target):
        found_in_line.append(i.start())
        # print("line", k, i.start(), i)
    full_line_found = (k, all_found_locations.append((k, found_in_line)))

# print(all_found_locations)


def xmas_search(charPos):
    global rows
    global pattern
    rev_pattern = pattern[::-1]
    found = 0
    for el in charPos:
        line = el[0]
        index_list = el[1]
        for id in index_list:
            if id >= 1 and id <= (len(rows[0]) - 2):
                s = rows[line - 1][id - 1] + \
                    pattern[1] + rows[line + 1][id + 1]
                if s == pattern or s == rev_pattern:
                    s = rows[line + 1][id - 1] + pattern[1] + \
                        rows[line - 1][id + 1]
                    if s == pattern or s == rev_pattern:
                        found += 1
                        print("line and id: ", line, id)
    return found


print(all_found_locations)
print(xmas_search(all_found_locations))
