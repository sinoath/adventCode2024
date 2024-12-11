f = open("../input.txt", "r")
row = []
for line in f:
    elements = []
    converted = []
    elements = line.split()
    for el in elements:
        converted.append(int(el))
    row.append(converted)
f.close()
dec, inc, diff = 0, 0, 0


def small_variation(data_list):
    """Input is a list, return True if adjacent int elements have
    a small variation between each other (at most three), False otherwise"""
    last_index = len(data_list) - 1
    global diff

    if last_index <= 0:
        return False
    while last_index > 0:
        diff = -1
        if abs(data_list[last_index] - data_list[last_index - 1]) > 3:
            diff = last_index
            return False
        last_index = last_index - 1
    return True


def dec_data(data_list):
    """Input is a list, return True if all int elements are
    strictly decreasing, False otherwise"""
    last_index = len(data_list) - 1
    global dec

    if last_index <= 0:
        return False
    while last_index > 0:
        dec = -1
        if data_list[last_index] >= data_list[last_index - 1]:
            dec = last_index
            return False
        last_index = last_index - 1
    return True


def inc_data(data_list):
    """Input is a list, return True if all int elements are
    strictly increasing, False otherwise"""
    last_index = len(data_list) - 1
    global inc

    if last_index <= 0:
        return False
    while last_index > 0:
        inc = -1
        if data_list[last_index] <= data_list[last_index - 1]:
            inc = last_index
            return False
        last_index = last_index - 1
    return True


second_chance = []
safe_anomaly_number = 0
for line in row:
    if (inc_data(line) or dec_data(line)) and small_variation(line):
        safe_anomaly_number = safe_anomaly_number + 1
    else:
        # print("Diff = {}, inc = {}, dec = {}".format(diff, inc, dec))
        second_chance.append(line)

print(safe_anomaly_number)
# print(second_chance)
single_bad_level_erased = []

for line in second_chance:
    test_line = line
    result = []
    for i in range(0, len(line)):
        # print("popping {}".format(i))
        temp_value = test_line.pop(i)
        # print(test_line)
        # print("pop ", test_line)
        if (inc_data(test_line) or dec_data(test_line)) and small_variation(test_line):
            safe_anomaly_number = safe_anomaly_number + 1
            break
        result.append(test_line)
        # print(result)
        test_line.insert(i, temp_value)
        # print("insert ", test_line)
    single_bad_level_erased.append(result)
    # print(single_bad_level_erased)
    # for el in single_bad_level_erased:
    #     if (inc_data(el) or dec_data(el)) and small_variation(el):
    #         safe_anomaly_number = safe_anomaly_number + 1
    #         break
# for i in range(0, 3):
#     print(single_bad_level_erased[i])
print(safe_anomaly_number)
