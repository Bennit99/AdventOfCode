from aocd import data, submit

result = 0
# data = '2333133121414131402'

disc = []
for i, c in enumerate(data):
    if i % 2 != 0:  # odd
        disc.extend(['.'] * int(c))
    else:  # even
        disc.extend([str(i // 2)] * int(c))

for i, c in enumerate(disc):
    if c == '.':
        while disc[-1] == '.':	
             disc.pop()
        disc[i] = disc.pop()


for i, c in enumerate(disc):
    result += i * int(c)
submit(result)