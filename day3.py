import regex as re
from day1 import read_file


def parse_data(data):
    valid = []
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    valid.extend(pattern.findall(data))
    return valid


def reduce_data(data):
    pattern = re.compile(r"do\(\)(.+?)don't\(\)")
    valid = []
    valid.extend(pattern.findall(data))
    return valid


def multiply(multiplication):
    multiplication = multiplication.replace("mul(", "")
    multiplication = multiplication.replace(")", "")
    num1, num2 = multiplication.split(",")
    return int(num1) * int(num2)


def calc_endresult(data):
    result = 0
    for line in data:
        result += multiply(line)
    return result


def main():
    data = read_file("day3_input.txt")
    data = "".join(data)
    valid = parse_data(data)
    return calc_endresult(valid)


def main_part_2():
    data = read_file("day3_input.txt")
    data = ["do()"] + data + ["don't()"]
    data = "".join(data)
    valid = reduce_data(data)
    valid = "".join(valid)
    valid = parse_data(valid)
    return calc_endresult(valid)


if __name__ == "__main__":
    print(main())
    print(main_part_2())