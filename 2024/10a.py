from aocd import data, submit

result = 0
data = [list(line) for line in data.splitlines()] # split data

# find zeros
zeros = set()
for r, row in enumerate(data):
    for c, cell in enumerate(row):
        if cell == '0':
            zeros.add((r, c))

# directions
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up

# check in every direction for one increase in height
def walk(r, c, h, tops): # row, column, height
    if h == 9: # reached mountain top
        tops.add((r, c))
        return
    for dr, dc in dir:
        if 0 <= r + dr < len(data) and 0 <= c + dc < len(data[0]) and data[r + dr][c + dc] == str(h + 1):
            walk(r + dr, c + dc, h + 1, tops) 

tops = set()
for r, c in zeros: # start at every zero
    tops.clear()
    walk(r, c, 0, tops)
    result += len(tops)

submit(result)