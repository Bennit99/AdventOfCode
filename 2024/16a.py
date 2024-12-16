from aocd import data, submit
import heapq

result = 0
map = [list(line) for line in data.splitlines()] # split data
map[1][len(map[0])-2] = '.' # remove end point


dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
start = (0, len(map)-2, 1, 0) # score, row, col, direction
end = (1, len(map[0])-2)
queue = [start]
visited = {(len(map)-2, 1, 0): 0} # row, col, direction

# find shortest path
while queue:
    s, r, c, d= heapq.heappop(queue)
    if (r, c) == end:
        result = s
        break
    for di, (dr, dc) in enumerate(dir):
        if map[r + dr][c + dc] == '.':
            s_next = s + (1 if di == d else 1001)
            if (r + dr, c + dc, di) in visited and visited[(r + dr, c + dc, di)] <= s_next:
                    continue
            visited[(r + dr, c + dc, di)] = s_next
            heapq.heappush(queue, (s_next, r + dr, c + dc, di))

print(result)
submit(result)