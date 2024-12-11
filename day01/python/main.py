first = []
second = []
f = open("../input.txt", "r")
for line in f:
    elements = line.split()
    first.append(int(elements[0]))
    second.append(int(elements[1]))
f.close()
first.sort()
second.sort()

result = 0
for i in range(0, len(first)):
    result = result + abs(first[i] - second[i])

print(result)

similarity = 0
for x in first:
    similarity = similarity + (x * second.count(x))
print(similarity)
