from aocd import data, submit

A = int(data.split('\n')[0].split()[-1])
result = ''

# run program
while A > 0:                            # 3(0)
    B = (A%8) ^ 1                       # 2(4=A), 1(1)
    C = A//(2**B)                       # 7(5=B)
    result += str(((B^5)^C)%8) + ','    # 1(5), 4(), 5(5=B)
    A = A//8                            # 0(3)

print(result[:-1])  # remove last comma
submit(result[:-1])