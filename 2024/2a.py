from aocd import get_data, submit

d = get_data(day=2, year=2024)

# split the data by space for every line
d = d.splitlines()
d = [list(map(int, line.split())) for line in d]
result = len(d)

for report in d:
    if report[0] > report[1]:
        report.reverse()
    for i in range(len(report)-1):
        if report[i+1] - report[i] not in [1, 2, 3]:
            result -= 1
            break

submit(result, part="a", day=2, year=2024)