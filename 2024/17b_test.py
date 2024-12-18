from aocd import data
import re

program = list(map(int, re.findall(r"\d+", data)))[3:]

A = 164278496489149

while A > 0:            # 3(0)
    B = (A%8) ^ 1       # 2(4=A), 1(1)
    C = A//(2**B)       # 7(5=B)
    print(((B^5)^C)%8)  # 1(5), 4(), 5(5=B)
    A = A//8            # 0(3)