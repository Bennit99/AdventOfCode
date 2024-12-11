from aocd import data, submit

stones = data.split(' ')
stones = [int(stone) for stone in stones]

n_blinks = 25

for i in range(n_blinks):
    new_stones = []
    for stone in stones:
        # rules
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.append(int(str(stone)[:len(str(stone))//2]))
            new_stones.append(int(str(stone)[len(str(stone))//2:]))
        else:
            new_stones.append(stone*2024)
    stones = new_stones

print(max(stones))
# submit(len(stones))