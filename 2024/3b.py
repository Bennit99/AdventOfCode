from aocd import get_data, submit
import re

result = 0
d = get_data(day=3, year=2024)
# d = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# Regex pattern to match mul(X,Y) where X and Y are 1-3 digit numbers or do() or don't()
pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"

# Find all matches in the string d
matches = re.findall(pattern, d)

# Process the matches
enabled = True
for x, y, do, dont in matches:
    if do:
        enabled = True
    elif dont:
        enabled = False
    elif enabled:
        result += int(x) * int(y)

submit(result, part="b", day=3, year=2024)