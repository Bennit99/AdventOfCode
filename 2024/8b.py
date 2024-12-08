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
    # combine 2 antenna
    for a1 in antenna:
        # add antennas itself as antinode
        result.add(a1)
        for a2 in antenna:
            if a1 != a2:
                # diff
                dr = a2[0] - a1[0] 
                dc = a2[1] - a1[1]
                r = a1[0]
                c = a1[1]
                while True: # add
                    r += dr
                    c += dc
                    if 0 <= r < len(data) and 0 <= c < len(data[0]): # check for out of bounce
                        result.add((r, c))
                    else:
                        break
                r = a1[0]
                c = a1[1]
                while True: # subtract
                    r -= dr
                    c -= dc
                    if 0 <= r < len(data) and 0 <= c < len(data[0]): # check for out of bounce
                        result.add((r, c))
                    else:
                        break

result = len(result)

submit(result)