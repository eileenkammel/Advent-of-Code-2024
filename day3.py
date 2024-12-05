import regex as re
from day1 import read_file


def parse_data(data):
    valid = []
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    for line in data:
        valid.extend(pattern.findall(line))
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
    valid = parse_data(data)
    return calc_endresult(valid)


if __name__ == "__main__":
    print(main())