from aocd import data, submit

result = 0
data = [list(line) for line in data.splitlines()]

# find indexes of '^' 
x_innit, y_innit = next((i, row.index('^')) for i, row in enumerate(data) if '^' in row)

# directions
dir = [(0, -1), (-1, 0), (0, 1), (1, 0)] # left, up, right, down
dir_i = 1 # direction index

for i in range(len(data)):
    if i % 10 == 0: 
        print(i)
    for j in range(len(data)):
        if data[i][j] not in ['#', '^']:
            data[i][j] = '#'
            x, y = x_innit, y_innit
            # walk the guard
            counter = 0
            dir_i = 1
            while True:
                counter += 1
                if counter > (len(data)/2): # loop detected
                    result += 1
                    break
                # check if map is finished
                if x+dir[dir_i][0] not in range(len(data)) or y+dir[dir_i][1] not in range(len(data[0])):
                    break
                # check if next cell is blocked
                if data[x+dir[dir_i][0]][y+dir[dir_i][1]] == '#':
                    dir_i = (dir_i + 1) % 4 # turn right
                else:   # move forward
                    x += dir[dir_i][0]
                    y += dir[dir_i][1]
            data[i][j] = '.' # reset map

submit(result)