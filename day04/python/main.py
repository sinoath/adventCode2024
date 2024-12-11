import re

file = open("../input.txt", "r")
rows = []
total_pattern_found = 0
line_index = -1

for line in file:
    rows.append(line)
    line_index += 1
file.close()


pattern = "XMAS"
rev_pattern = pattern[::-1]
pattern_max_index = len(pattern) - 1


def complete_horizontal_search(s):
    global pattern
    global rev_pattern
    times_found = 0
    occurencies = re.findall(pattern, s)
    reverse_occur = re.findall(rev_pattern, s)
    times_found = len(occurencies) + len(reverse_occur)
    if times_found:
        return times_found
    else:
        return 0


for el in rows:
    total_pattern_found += complete_horizontal_search(el)


# Find all first letter occurencies for 'pattern' (XMAS)
all_found_locations = []
full_line_found = ()
for k in range(0, len(rows)-len(pattern)+1):
    found_in_line = []
    search_target = rows[k]
    for i in re.finditer(pattern[0], search_target):
        found_in_line.append(i.start())
        # print("line", k, i.start(), i)
    full_line_found = (k, all_found_locations.append((k, found_in_line)))


# Find al first letter occurencies for 'rev_pattern' (SAMX)
rev_found_locations = []
full_line_found = ()
for k in range(0, len(rows)-len(rev_pattern)+1):
    found_in_line = []
    search_target = rows[k]
    for i in re.finditer(rev_pattern[0], search_target):
        found_in_line.append(i.start())
    full_line_found = (k, rev_found_locations.append((k, found_in_line)))


def oblique_search(targetString, first_chars):
    forward = 0
    backward = 0
    global rows

    # oblique forward search
    for el in first_chars:
        line = el[0]
        index_list = el[1]
        # if index_list != []:
        for id in index_list:
            if id <= (len(rows[0]) - len(targetString)):
                s = targetString[0]
                for i in range(1, len(targetString)):
                    s += rows[line+i][id+i]
                if s == targetString:
                    forward += 1

    # oblique backward search
    for el in first_chars:
        line = el[0]
        index_list = el[1]
        if index_list != []:
            for id in index_list:
                if id >= (len(targetString) - 1):  # (4 - 1)
                    s = targetString[0]
                    for i in range(1, len(targetString)):
                        s += rows[line+i][id-i]
                    if s == targetString:
                        backward += 1
    return forward + backward


def vert_search(targetString, first_chars, lines):
    global rows
    found = 0
    for el in first_chars:
        line = el[0]
        index_list = el[1]
        if index_list != []:
            for id in index_list:
                s = targetString[0]
                for i in range(1, len(targetString)):
                    s += lines[line+i][id]
                if s == targetString:
                    found += 1
    return found


hori, vert, obl = 0, 0, 0

counter = 0
for line in rows:
    counter += 1
    hori += complete_horizontal_search(line)
    # print("line and value: ", counter, hori)
print("horizontal: ", hori)
# print(complete_horizontal_search(rows[0]))
vert += vert_search(pattern, all_found_locations, rows)
vert += vert_search(rev_pattern, rev_found_locations, rows)
obl += oblique_search(pattern, all_found_locations)
obl += oblique_search(rev_pattern, rev_found_locations)
print("oblique: ", obl)
print("vert: ", vert)
print("total: ", vert + hori + obl)
