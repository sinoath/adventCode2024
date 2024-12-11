import re

file = open("../test2.txt", "r")
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


def hori_search(s):
    global pattern
    times_found = 0
    occurencies = re.findall(pattern, s)
    reverse_occur = re.findall(rev_pattern, s)
    times_found = len(occurencies) + len(reverse_occur)
    if times_found:
        return times_found
    else:
        return 0


for el in rows:
    total_pattern_found += hori_search(el)

# print(total_pattern_found)
# print(line_index)
# test_regex_indexes = re.findall(pattern[0], rows[3])
# test_regex_indexes = re.findall(pattern[0], rows[4])
# res = re.search(pattern[0], rows[0])
# alt_res = re.search(pattern[0], rows[4])

# print(test_regex_indexes)
all_found_locations = []
full_line_found = ()
# print(line_index, pattern_max_index)
# print(len(rows), len(pattern))
for k in range(0, len(rows)-len(pattern)+1):
    found_in_line = []
    search_target = rows[k]
    for i in re.finditer(pattern[0], search_target):
        if i.start():
            found_in_line.append(i.start())
        # print("line", k, i.start(), i)
    full_line_found = (k, all_found_locations.append((k, found_in_line)))
# print(all_found_locations)

found = 0
tpl_el = all_found_locations[3]
line = tpl_el[0]
indexes = tpl_el[1]
print(all_found_locations)
# print(line, indexes)

# ### working search vertically
# s = pattern[0]
# for i in range(1, len(pattern)):
#     # print(line, i)
#     s = s + rows[line+i][indexes[0]]
#     if s == pattern:
#         found += 1

# search vertically
# s = pattern[0]
for el in all_found_locations:
    line = el[0]
    index_list = el[1]
    print(line, index_list)
    if index_list != []:
        for id in index_list:
            s = pattern[0]
            for i in range(1, len(pattern)):
                # print(line, i)
                s = s + rows[line+i][id]
            if s == pattern:
                print(s)
                found += 1

print("found: ", found)
# search forward oblique
s = pattern[0]
tpl_el = all_found_locations[0]
line = tpl_el[0]
indexes = tpl_el[1]
for i in range(1, len(pattern)):
    # print("oblique", i)
    s += rows[line + i][indexes[0] + i]
# print("Oblique forward: ", s)
