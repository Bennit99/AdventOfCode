from aocd import data, submit

result = 0
room, moves = data.split("\n\n") # Split the string into room and moves
room = [list(line) for line in room.splitlines()] # split data
moves = moves.replace("\n", "") # remove newlines

# Define the replacement rules
replacement_rules = {
    '#': '##',
    'O': '[]',
    '.': '..',
    '@': '@.'
}

# Widen the room according to the rules
for i, row in enumerate(room):
    widened_row = []
    for tile in row:
        widened_row.extend(replacement_rules.get(tile))
    room[i] = widened_row


d = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)} # up, down, right, left
# Find the robot
rob = next([r, c] for r, row in enumerate(room) for c, val in enumerate(row) if val == '@')

def move_box(r, c, d):
    if room[r][c] == ']':   # locate box
        c -= 1
    room[r][c] = '.'        # delete box
    room[r][c+1] = '.'  
    room[r + d[0]][c + d[1]] = '['  # move box
    room[r + d[0]][c+1 + d[1]] = ']'     

def check_push(r, c, d):
    if room[r][c] == ']':   # locate box
        c -= 1
    if (r, c) not in checks:    # skip duplicate checks
        checks.add((r, c))
    else:
        return []
    result = [(r, c)]
    if d[0] == 0: # horizontal
        if d == (0, 1):
            d = (0, 2)
        if room[r][c + d[1]] == '#':    # wall
            return [False]
        if room[r][c + d[1]] in ['[', ']']:   # another box
            result = check_push(r, c + d[1], d) + result
        return result
    else: # vertical
        le = room[r + d[0]][c]
        ri = room[r + d[0]][c+1]
        if le == '#' or ri == '#':    # wall
            return [False]
        if le in ['[', ']']:
            result = check_push(r + d[0], c, d) + result
        if ri == '[':
            result = check_push(r + d[0], c+1, d) + result
        return result

for m in moves:
    r = rob[0] + d[m][0]  # row 
    c = rob[1] + d[m][1] # column
    if room[r][c] == '#': # wall
        continue
    if room[r][c] in ['[', ']']:
        checks = set()
        boxes = check_push(r, c, d[m])
        if False in boxes:
            continue
        else:
            if m == '^':            # move boxes in the right order
                boxes.sort(key=lambda x: x[0])
            elif m == 'v':
                boxes.sort(key=lambda x: x[0], reverse=True)
            for box in boxes:
                move_box(*box, d[m])
    room[rob[0]][rob[1]] = '.'  # move robot
    rob = [r, c]
    room[r][c] = '@'


# count GPS coordinates
for i, r in enumerate(room):
    for j, c in enumerate(r):
        if c == '[':
            result += 100 * i + j

print(result)
submit(result)