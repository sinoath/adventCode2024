import re

file = open("../input.txt", "r")
content_of_file = ""
# content_of_file = []
# for line in file:
#     content_of_file.append(line)
content_of_file = file.read()
file.close()
starting_point, dont, does = 0, 0, 0
while dont >= 0 and does >= 0:
    dont = content_of_file.find("don't()", starting_point)
    does = content_of_file.find("do()", dont)
    if dont < does and does >= 0:
        memory_chunks = content_of_file[0:dont +
                                        1] + content_of_file[does + 1:]
    starting_point = does
# print(content_of_file.find("randomstring"))
# print(content_of_file)
print(content_of_file.find("don't()", starting_point))

# print(memory_chunks)
# print(dont, does)


pattern = "mul\(+([0-9]?[0-9]?[0-9]),+([0-9]?[0-9]?[0-9])\)"
all_mult = re.findall(
    pattern,
    memory_chunks
)
# print(all_mult)

total = 0
couples = []
for el in all_mult:
    first = int(el[0])
    second = int(el[1])
    total = total + (first * second)
    # print(first, "  ", second)
    couples.append((first, second))

# print(type(all_mult))
# print(couples)
print("Total: ", total)
# preceding result was 167661529
