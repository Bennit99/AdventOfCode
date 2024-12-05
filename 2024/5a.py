from aocd import get_data, submit

result = 0
d = get_data(day=5, year=2024)

# Split the string into lines
d = d.splitlines()

# Split the lines into two parts
r = d[:d.index('')]
u = d[d.index('')+1:]

# Split each line by the delimiter and convert to a list of lists
r = [list(map(int, line.split('|'))) for line in r]
us = [list(map(int, line.split(','))) for line in u]

# create a list from the middle values of the lists in u
result = [update[int((len(update))/2)] for update in us]

for i, u in enumerate(us):  # go thru update list
    for a, b in r:          # check rules
        if a in u and b in u and u.index(a) > u.index(b):
            result[i] = 0
            break

result = sum(result)

submit(result, part="a", day=5, year=2024)