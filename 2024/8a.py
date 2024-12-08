from aocd import data, submit

result = set()
data = [list(line) for line in data.splitlines()]

# find unique chars in data
chars = set()
for row in data:
    for char in row:
        chars.add(char)
chars.remove('.')

for char in chars:
    # find antenna position
    antenna = set()
    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            if cell == char:
                antenna.add((r, c))
    # combine
    for a1 in antenna:
        for a2 in antenna:
            if a1 != a2:
                # diff
                diff = (a2[0] - a1[0], a2[1] - a1[1])
                result.add((a1[0] - diff[0], a1[1] - diff[1]))
                result.add((a2[0] + diff[0], a2[1] + diff[1]))

# filter out of bound values
valid_result = set()
for r, c in result:
    if 0 <= r < len(data) and 0 <= c < len(data[0]):
        valid_result.add((r, c))
result = valid_result
    
# count elements in result
result = len(result)

submit(result)