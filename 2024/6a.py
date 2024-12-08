from aocd import data, submit

result = 0
data = [list(line) for line in data.splitlines()]

# find indexes of '^' 
x, y = next((i, row.index('^')) for i, row in enumerate(data) if '^' in row)

# directions
dir = [(0, -1), (-1, 0), (0, 1), (1, 0)] # left, up, right, down
dir_i = 1 # direction index

# walk the guard
while True:
    data[x][y] = 'X' # mark as visited
    # check if map is finished
    if x+dir[dir_i][0] not in range(len(data)) or y+dir[dir_i][1] not in range(len(data[0])):
        break
    # check if next cell is blocked
    if data[x+dir[dir_i][0]][y+dir[dir_i][1]] == '#':
        dir_i = (dir_i + 1) % 4 # turn right
    else:   # move forward
        x += dir[dir_i][0]
        y += dir[dir_i][1]

# count 'X' in data
result = sum(row.count('X') for row in data)

submit(result)