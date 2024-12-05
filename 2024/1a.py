from aocd import get_data, submit
import numpy as np

d = get_data(day=1, year=2024)
result = 0

# split the data by space for every line
l, r = zip(*(line.split('   ') for line in d.splitlines()))

# convert to numpy array
l = np.array(l).astype(int)
r = np.array(r).astype(int)

# sort
l = np.sort(l)
r = np.sort(r)

result = np.sum(abs(l - r))
print(result)
submit(result, part="a", day=1, year=2024)