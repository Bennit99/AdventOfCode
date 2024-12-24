from aocd import data, submit

result = 0
data = [int(line) for line in data.splitlines()]

iterations = 2000
price = []

for secret in data:
    p = [(0, secret % 10)]
    for i in range(iterations):
        secret = (secret ^ (secret << 6)) & (2**24 - 1)
        secret = (secret ^ (secret >> 5)) & (2**24 - 1)
        secret = (secret ^ (secret << 11)) & (2**24 - 1)
        digit = secret % 10
        p.append((digit - p[-1][1], digit))
    p = p[1:]
    price.append(p)

for a in range(-9, 10):
    for b in range(-9, 10):
        print(a,b)
        if not -9 <= a+b <= 9:
            continue
        for c in range(-9, 10):
            if not -9 <= sum((a, b, c)) <= 9 or not -9 <= b+c <= 9:
                continue
            for d in range(0, 10):
                if 0 <= sum((a, b, c, d)) <= 9 and 0 <= b+c+d <= 9 and 0 <= c+d <= 9: # experimental: sort out unlikely values where 9 bananas not possible
                    bananas = 0
                    for p in price:
                        for i in range(len(p)-3):
                            if a == p[i][0] and b == p[i+1][0] and c == p[i+2][0] and d == p[i+3][0]:
                                bananas += p[i+3][1]
                                break
                    result = max(result, bananas)

print(result)
submit(result)
