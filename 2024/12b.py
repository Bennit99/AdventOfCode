from aocd import data, submit
import time

start_time = time.time()
result = 0
data = [list(line) for line in data.splitlines()] # split data

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
visited = set()
field_type = ''
field_area = set()
fence = set()

def walk_field(r, c, r_prev, c_prev):
    if 0 <= r < len(data) and 0 <= c < len(data[r]) and data[r][c] == field_type and (r, c) not in visited:
        visited.add((r, c))
        field_area.add((r, c))
        for d in dir:
            walk_field(r + d[0], c + d[1], r, c)
    elif (r, c) not in field_area:
        fence.add(((r+r_prev)/2, (c+c_prev)/2))

def apply_discount():
    disc_fence = 0
    for r, c in fence:
        if r % 1 == 0: # fence is horizontal
            # skip counting if fence is continuing east, except for special case of cross fence
            if (r+1, c) not in fence or (r+0.5, c+0.5) in fence:
                disc_fence += 1
        else: # fence is vertical
            # skip counting if fence is continuing south, except for special case of cross fence
            if (r, c+1) not in fence or (r+0.5, c+0.5) in fence:
                disc_fence += 1
    return disc_fence

for r in range(len(data)):
    for c in range(len(data[r])):
        if (r,c) not in visited:
            field_type = data[r][c]
            walk_field(r, c, None, None)
            disc_fence = apply_discount()
            result += len(field_area) * disc_fence
            field_area.clear()
            fence.clear()

print(f"Time taken: {round(time.time() - start_time, 4)} seconds")
submit(result)