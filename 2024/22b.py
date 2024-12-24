from aocd import data, submit
from collections import Counter, deque

data = [int(line) for line in data.splitlines()]
bananas = Counter()

def next_secret(secret: int) -> int:
    secret = (secret ^ (secret << 6)) & 0xFFFFFF
    secret = (secret ^ (secret >> 5)) & 0xFFFFFF
    return (secret ^ (secret << 11)) & 0xFFFFFF

for secret in data:
    dict = {}
    seq = deque(maxlen=4)
    prev_price = secret % 10
    for i in range(2000):
        secret = next_secret(secret)
        price = secret % 10
        seq.append(price - prev_price)
        seq_tuple = tuple(seq)
        if i >= 4 and seq_tuple not in dict:
            dict[seq_tuple] = price
        prev_price = price
    bananas.update(dict)

print(bananas.most_common(1)[0][1])
submit(bananas.most_common(1)[0][1])
