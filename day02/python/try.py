file = open("../test.txt", "r")
row = []

for line in file:
    content = map(int, line.split())
    row.append(list(content))

print(row)


def single_level_erased(my_list):
    result = []
    for i in range(len(my_list))
    temp_list = my_list
    temp_list.remove(x)
    result.append(temp_list)
    return result


third_row_with_tolerance = single_level_erased(row[2])
print(third_row_with_tolerance)
