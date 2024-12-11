import re

file = open("../input.txt", "r")
content_of_file = ""
content_of_file = file.read()
file.close()

cleaned_memory = ""
memory_chunks = content_of_file.split("don't()")
cleaned_memory = cleaned_memory + memory_chunks[0]

print(memory_chunks)
print(cleaned_memory)
memory_chunks.pop(0)
print(memory_chunks)
for el in memory_chunks:
    found = el.find("do()")
    if found:
        cleaned_memory = cleaned_memory + el[found:]


pattern = "mul\(+([0-9]?[0-9]?[0-9]),+([0-9]?[0-9]?[0-9])\)"
all_mult = re.findall(
    pattern,
    cleaned_memory
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

print(type(all_mult))
print(couples)
print("Total: ", total)
