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


def small_variation(data_list):
    """Input is a list, return True if adjacent int elements have
    a small variation between each other (at most three), False otherwise"""
    last_index = len(data_list) - 1

    if last_index <= 0:
        return False
    while last_index > 0:
        if abs(data_list[last_index] - data_list[last_index - 1]) > 3:
            return False
        last_index = last_index - 1
    return True


def dec_data(data_list):
    """Input is a list, return True if all int elements are
    strictly decreasing, False otherwise"""
    last_index = len(data_list) - 1

    if last_index <= 0:
        return False
    while last_index > 0:
        if data_list[last_index] >= data_list[last_index - 1]:
            return False
        last_index = last_index - 1
    return True


def inc_data(data_list):
    """Input is a list, return True if all int elements are
    strictly increasing, False otherwise"""
    last_index = len(data_list) - 1

    if last_index <= 0:
        return False
    while last_index > 0:
        if data_list[last_index] <= data_list[last_index - 1]:
            return False
        last_index = last_index - 1
    return True


safe_anomaly_number = 0
for line in row:
    if (inc_data(line) or dec_data(line)) and small_variation(line):
        safe_anomaly_number = safe_anomaly_number + 1

print(safe_anomaly_number)
