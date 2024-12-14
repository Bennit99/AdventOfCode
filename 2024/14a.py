from aocd import data, submit
import re

result = 0
data = data.split("\n")
robots = [tuple(map(int, re.findall(r"-?\d+", problem))) for problem in data]

r_len = 103 # 7
c_len = 101 # 11
seconds = 100

quadrants = [[0, 0], [0, 0]]

for c, r, cv, rv in robots:                     # calculate ech robot severalty
    r = (r + (rv + r_len) * seconds) % r_len    # run row for 100 seconds
    c = (c + (cv + c_len) * seconds) % c_len    # run column for 100 seconds
    if r == r_len//2 or c == c_len//2:          # ignore the center lines
        continue
    r = 0 if r < r_len // 2 else 1
    c = 0 if c < c_len // 2 else 1
    quadrants[r][c] += 1

result = quadrants[0][0] * quadrants[0][1] * quadrants[1][0] * quadrants[1][1]
submit(result)