from aocd import data, submit
import time

start_time = time.time()
result = 0
data = [list(line) for line in data.splitlines()] # split data

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
visited = set()
field_type = ''
field_area = set()
fence = 0

def walk_field(r, c):
    if 0 <= r < len(data) and 0 <= c < len(data[r]) and data[r][c] == field_type and (r, c) not in visited:
        visited.add((r, c))
        field_area.add((r, c))
        for d in dir:
            walk_field(r + d[0], c + d[1])
    elif (r, c) not in field_area:
        global fence
        fence += 1

for r in range(len(data)):
    for c in range(len(data[r])):
        if (r,c) not in visited:
            field_type = data[r][c]
            walk_field(r, c)
            result += len(field_area) * fence
            field_area.clear()
            fence = 0

print(f"Time taken: {round(time.time() - start_time, 4)} seconds")

submit(result)