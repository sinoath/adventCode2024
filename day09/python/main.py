f = open("../test.txt", "r")
content = (f.readline()).strip()
f.close()
print(len(content))
print(content)

expandedString = ""
for i in range(len(content)):
    if i % 2 == 0:
        print(str(i // 2) * int(content[i]))
        expandedString += (str(i // 2) * int(content[i]))
    else:
        print("." * int(content[i]))
        expandedString += ("." * int(content[i]))

print(expandedString)
