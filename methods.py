def count_info(data_dict, info):
    count = 0
    for e in range(1, len(data_dict)+1):
        for el in range(len(data_dict[e])):
            if data_dict[e][el] == info:
                count += 1
    return count


def find_info(data_dict, info):
    for value in data_dict.values():
        for el in value:
            if el == info:
                return value


def del_info(data_dict, info):
    for key, value in data_dict.items():
        if info in value:
            data_dict.pop(key)
            return data_dict
