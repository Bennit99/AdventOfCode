from aocd import data, submit

result = 0
# data = '2333133121414131402'

disc = []
for i, c in enumerate(data):
    if i % 2 != 0:  # odd
        disc.append(['.', int(c)])
    else:  # even
        disc.append([i // 2, int(c)])

stupid_ausgleich_var = 0
for j, f in enumerate(reversed(disc)):
    if f[0] != '.':
        for i, e in enumerate(disc[:-j-1-stupid_ausgleich_var]):
            if e[0] == '.' and e[1] >= f[1]:
                disc.insert(i, f.copy())# insert f into empty space
                f[0] = '.'              # remove file
                e[1] = e[1] - f[1]      # remove empty space
                stupid_ausgleich_var+=1 # adjust index
                break

list = []
for c, n in disc:
    for j in range(n):
        list.append(c)


for i, c in enumerate(list):
    if c != '.':
        result += i * int(c)
submit(result)