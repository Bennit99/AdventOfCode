from aocd import get_data, submit

d = get_data(day=2, year=2024)

# split the data by space for every line
d = d.splitlines()
d = [list(map(int, line.split())) for line in d]
result = 0

for report in d:    # for every report
    for i in range(len(report)):    # for every element in the report
        x = report[:i] + report[i+1:]   # remove the i-th element
        if x[0] > x[1]:
            x.reverse()
        for i in range(len(x)-1): # check every element pair
            if x[i+1] - x[i] not in [1, 2, 3]:
                break
        else:  # if the loop didn't break
            result += 1
            break

submit(result, part="b", day=2, year=2024)