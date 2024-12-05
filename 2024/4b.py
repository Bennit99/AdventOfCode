from aocd import data, submit
import numpy as np

result = 0
d = data
a = np.array([list(line) for line in d.splitlines()])

for i in range(1, len(a) - 1):
    for j in range(1, len(a[0]) - 1):
        if (a[i][j] == "A" and      # A
            {a[i-1][j-1], a[i+1][j+1]} == {a[i-1][j+1], a[i+1][j-1]} == {"M", "S"}):    # M S
            result += 1        

submit(result, part="b", day=4, year=2024)