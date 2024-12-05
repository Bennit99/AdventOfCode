from aocd import get_data, submit
import re

result = 0
d = get_data(day=3, year=2024)
# d = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# Regex pattern to match mul(X,Y) where X and Y are 1-3 digit numbers
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Find all matches in the string d
matches = re.findall(pattern, d)

# Process the matches
for match in matches:
    x, y = map(int, match)
    result += x * y

submit(result, part="a", day=3, year=2024)