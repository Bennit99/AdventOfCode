from aocd import data, submit
import time
import matplotlib.pyplot as plt
import heapq

result = 0
map = [list(line) for line in data.splitlines()] # split data
map[1][len(map[0])-2] = '.' # remove end point


# Optional: remove dead ends
start_time = time.time()
total_changes = 0
while True:
    changed = 0
    for y in range(1, len(map)):
        for x in range(1, len(map[y])):
            if map[y][x] == '.':
                walls = sum([map[y][x - 1] == '#', map[y][x + 1] == '#', map[y - 1][x] == '#', map[y + 1][x] == '#'])
                if walls >= 3:
                    map[y][x] = '#'
                    changed += 1
    total_changes += changed
    if not changed:
        break
print('Removed', total_changes, 'dead ends in', round(time.time() - start_time, 4), 'seconds')

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
start = (0, len(map)-2, 1, 0) # row, col, direction, score
end = (1, len(map[0])-2)
queue = [start]
visited = {(len(map)-2, 1, 0): 0} # row, col, direction

# find shortest path
while queue:
    s, r, c, d= heapq.heappop(queue)
    if (r, c) == end:
        shortest_path = s
        break
    for di, (dr, dc) in enumerate(dir):
        if map[r + dr][c + dc] == '.':
            s_next = s + (1 if di == d else 1001)
            if (r + dr, c + dc, di) in visited and visited[(r + dr, c + dc, di)] <= s_next:
                    continue
            visited[(r + dr, c + dc, di)] = s_next
            heapq.heappush(queue, (s_next, r + dr, c + dc, di))


# get visited by partial key
def get_visited(visited, r=None, c=None, d=None, s=None):
    return [value for (R, C, D), value in visited.items()
            if (r is None or r == R) and 
            (c is None or c == C) and 
            (d is None or d == D) and 
            (s is None or value in s)]

# mark path
Q = [(1, len(map[0])-2, shortest_path)] # r, c, score
for p in Q:
    map[p[0]][p[1]] = 'O'
    for di, (dr, dc) in enumerate(dir):
            next_p = (p[0] + dr, p[1] + dc)
            for v in get_visited(visited, r=next_p[0], c=next_p[1], s=(p[2]-1, p[2]-1001)):
                next_p = (next_p[0], next_p[1], v)
                if next_p not in Q:
                    Q.append(next_p)

# remove double paths with different directions
path = set()
for p in Q:
    path.add((p[0], p[1])) 

# plot map 
# '#' = black, '.' = white, 'O' = red
color_map = []
for line in map:
    color_line = []
    for c in line:
        if c == '#':
            color_line.append([0, 0, 0])
        elif c == 'O':
            color_line.append([255, 0, 0])
        else:
            color_line.append([255, 255, 255])
    color_map.append(color_line)
plt.imshow(color_map, interpolation='nearest')
plt.axis('off')  # Turn off the axis
plt.show()

print(len(path))
# submit(result)