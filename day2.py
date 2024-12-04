from day1 import read_file


def make_pairs(report):
    pairs = [(report[i], report[i+1]) for i in range(len(report)-1)]
    return pairs


def analyze_report(report):
    report_pairs = make_pairs(report)
    results = []
    for pair in report_pairs:
        results.append(pair_comparison(pair))
    results = set(results)
    print(results)
    return 1 if len(results) == 1 else 0


def check_difference(pair):
    difference = abs(pair[0] - pair[1])
    return True if difference in [1, 2, 3] else False


def check_for_increase(pair):
    return pair[0] < pair[1]


def pair_comparison(pair):
    if check_difference(pair):
        return check_for_increase(pair)


def find_safe_reports():
    data = read_file("day2_input.txt")
    print(data)
    valid_reports = 0
    for report in data:
        report = report.split()
        report = [int(num) for num in report]
        print(report)
        valid_reports += analyze_report(report)
    return valid_reports


if __name__ == "__main__":
    print(find_safe_reports())
