from aocd import data, submit


data = [list(line) for line in data.splitlines()] # Split the string into lines

# Find start and end points
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == 'S':
            start = (r, c, 0)
        elif data[r][c] == 'E':
            end = (r, c)
visited = {(start[0], start[1]): 0} # row, col, score
Q = [start]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
R, C = len(data), len(data[0]) # length row and column

# dikstra's algorithm for shortest path
while Q:
    r, c, s = Q.pop(0)
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if (nr, nc) == end:
            visited[(nr, nc)] = s + 1
            Q.clear()
            break
        if 0 <= nr < R and 0 <= nc < C and (nr,nc) not in visited and data[nr][nc] == '.':
            visited[(nr, nc)] = s + 1
            Q.append((nr, nc, s + 1))

shortest_path = visited[end]

# mark path
Q = [(end[0], end[1], shortest_path)] # r, c, score
for r, c, s in Q:
    data[r][c] = s
    for dr, dc in dir:
            next_p = (r + dr, c + dc)
            if next_p in visited and visited[next_p] == s - 1:
                Q.append((r + dr, c + dc, s - 1))

shortcuts = []

# find shortcuts
for r in range(R):
    for c in range(C):
        if data[r][c] != '#':
            for i in range(-20, 21):    # search in a 20 field radius circle
                for j in range(-20, 21):
                    if abs(i) + abs(j) > 20:
                        continue
                    next_r, next_c = r + i, c + j
                    cheat_length = abs(i) + abs(j)
                    if 0 <= next_r < R and 0 <= next_c < C and data[next_r][next_c] != '#':
                        if data[r][c] + 99 + cheat_length < data[next_r][next_c]:
                            shortcuts.append(data[next_r][next_c]- data[r][c] - cheat_length)

print(len(shortcuts))
submit(len(shortcuts))