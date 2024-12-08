from aocd import data, submit
import re

result = 0
data = [list(map(int, re.split(r':?\s+', line))) for line in data.splitlines()] # split data

def calc(x, t, n) -> bool:
    a = x + n[0]
    b = x * n[0]
    n = n[1:]
    if len(n) == 0:
        return a == t or b == t
    else:
        return calc(a, t, n) or calc(b, t, n)

for line in data:
    t = line[0]
    x = line[1]
    if calc(x, t, line[2:]):
        result += t


submit(result)