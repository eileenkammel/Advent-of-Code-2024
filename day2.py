
from day1 import read_file


def make_pairs(report):
    pairs = [(report[i], report[i+1]) for i in range(len(report)-1)]
    return pairs


def analyze_report(report: list[int], dampened):
    report_pairs = make_pairs(report)
    results = []
    for pair in report_pairs:
        results.append(pair_comparison(pair))
    results = list(set(results))
    if len(results) == 1 and results[0] is not None:
        return 1
    if dampened:
        for i in range(len(report)):
            reduced_report = report[:]
            reduced_report.pop(i)
            assert len(reduced_report) == len(report) - 1
            reduced_pairs = make_pairs(reduced_report)
            reduced_results = [pair_comparison(pair) for pair in reduced_pairs]
            reduced_results = list(set(reduced_results))
            if len(reduced_results) == 1 and reduced_results[0] is not None:
                return 1
    return 0


def check_difference(pair):
    difference = abs(pair[0] - pair[1])
    return True if difference in [1, 2, 3] else False


def check_for_increase(pair):
    return pair[0] < pair[1]


def pair_comparison(pair):
    if check_difference(pair):
        return check_for_increase(pair)


def find_safe_reports(dampened):
    data = read_file("day2_input.txt")
    valid_reports = 0
    for report in data:
        report = report.split()
        report = [int(num) for num in report]
        delta = analyze_report(report, dampened)
        if delta:
            print("SAFE")
        else:
            print("UNSAFE")
        valid_reports += delta
    return valid_reports


if __name__ == "__main__":
    print(find_safe_reports(dampened=False))
    print(find_safe_reports(dampened=True))
