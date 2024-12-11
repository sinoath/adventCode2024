import re

file = open("../input.txt", "r")
content_of_file = ""
# content_of_file = []
# for line in file:
#     content_of_file.append(line)
content_of_file = file.read()
file.close()
pattern = "mul(\(+[0-9]?[0-9]?[0-9]),+([0-9]?[0-9]?[0-9]\))"
all_mult = re.findall(
    pattern,
    content_of_file
)
print(all_mult)

total = 0
couples = ()
for el in all_mult:
    first = int(el[0][1:])
    second = int(el[1][:-1])
    total = total + (first * second)
    print(first, "  ", second)

print("Total: ", total)
