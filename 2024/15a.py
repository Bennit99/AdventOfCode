from aocd import data, submit

result = 0
room, moves = data.split("\n\n") # Split the string into room and moves
room = [list(line) for line in room.splitlines()] # split data
moves = moves.replace("\n", "") # remove newlines

d = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)} # up, down, right, left
# Find the robot
rob = next([r, c] for r, row in enumerate(room) for c, val in enumerate(row) if val == '@')

for m in moves:
    r = rob[0]  # row 
    c = rob[1]  # column
    while True: # push
        r += d[m][0] # row 
        c += d[m][1] # column
        if room[r][c] == '#': # wall
            break
        if room[r][c] == '.':
            room[r][c] = 'O'            # push box
            room[rob[0]][rob[1]] = '.'  # move robot
            rob[0] = rob[0] + d [m][0]
            rob[1] = rob[1] + d [m][1]
            room[rob[0]][rob[1]] = '@'
            break

# count GPS coordinates
for i, r in enumerate(room):
    for j, c in enumerate(r):
        if c == 'O':
            result += 100 * i + j

submit(result)