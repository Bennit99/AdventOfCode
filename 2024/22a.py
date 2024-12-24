from aocd import data, submit

result = 0
data = [int(line) for line in data.splitlines()]

iterations = 2000

for secret in data:
    for i in range(iterations):
        secret = (secret ^ (secret << 6)) & (2**24 - 1)
        secret = (secret ^ (secret >> 5)) & (2**24 - 1)
        secret = (secret ^ (secret << 11)) & (2**24 - 1)
    result += secret
submit(result)