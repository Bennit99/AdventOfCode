from aocd import data, submit
import re
result = 0
data = data.split("\n\n")
eqs = [tuple(map(int, re.findall(r"\d+", problem))) for problem in data]

for a1, a2, b1, b2, p1, p2 in eqs:
    x2 = (a1*p2 - a2*p1) / (b2*a1 - b1*a2)
    x1 = (p1 - b1*x2) / a1
    if x1 % 1 == 0 and x2 % 1 == 0:
        result += x1*3 + x2

submit(result)