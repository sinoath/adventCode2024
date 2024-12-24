f = open("../test.txt", "r")
conten = []
for line in f:
    content = line.strip("\n")
f.close()

stones = content.split(" ")
print(stones)
