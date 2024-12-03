# Advent of Code - Day 1

def read_file(file):
    with open(file) as f:
        data = f.read().splitlines()
    return data


def split_lst(lst):
    list1 = []
    list2 = []
    for element in lst:
        element = element.split()
        list1.append(int(element[0]))
        list2.append(int(element[1]))

    return list1, list2


def sort_lists(lst1, lst2):
    # Sort in ascending order
    lst1.sort()
    lst2.sort()
    return lst1, lst2


def make_pairs(lst1, lst2):
    pairs = zip(lst1, lst2)
    return pairs


def calc_difference(pair):
    diff = abs(pair[1] - pair[0])
    return diff


def sum_diff(pairs):
    sum = 0
    for pair in pairs:
        sum += calc_difference(pair)
    return sum


def find_occurance_count(lst, num):
    return lst.count(num)


def clac_similarity(num, occurances):
    return (num * occurances)


def main_part_1(filename):
    data = read_file(filename)
    list1, list2 = split_lst(data)
    list1, list2 = sort_lists(list1, list2)
    pairs = make_pairs(list1, list2)
    sum = sum_diff(pairs)
    print(sum)


def main_part_2(filename):
    similarity_sum = 0
    data = read_file(filename)
    list1, list2 = split_lst(data)
    for num in list1:
        occurances = find_occurance_count(list2, num)
        similarity_sum += clac_similarity(num, occurances)
    print(similarity_sum)





if __name__ == "__main__":
    main_part_1("day1_input.txt")
    main_part_2("day1_input.txt")
