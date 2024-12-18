from aocd import data, submit

result = 0
data = data.splitlines() # Split the string into lines
data = [line.split(',') for line in data] # Split the lines into lists
data = [(int(r), int(c)) for c, r in data] # Convert the strings into integers

map_size = 71
map = [['.' for i in range(map_size)] for j in range(map_size)] # Create map

bytes = 1024
for r, c in data[:bytes]:
    map[r][c] = '#'

start = (0, 0, 0) # (row, column, steps)
end = (map_size-1, map_size-1)
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up

for y, x in data[bytes:]:
    map[y][x] = '#'
    Q = [start]
    visited = {}
    path = False
    # dikstra's algorithm
    while Q:
        r, c, s = Q.pop(0)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) == end:
                Q.clear()
                path = True
                break
            if 0 <= nr < map_size and 0 <= nc < map_size and (nr,nc) not in visited and map[nr][nc] == '.':
                visited[(nr, nc)] = s + 1
                Q.append((nr, nc, s + 1))
    if not path:
        result = str(x) + ',' + str(y)
        break

print(result)
submit(result)