from aocd import data, submit
from functools import cache

result = 0
towels, designs = data.split("\n\n")
towels = towels.split(", ")
designs = designs.split("\n")


@cache
def add_towel(design):
    return sum(
        towel == design[:len(towel)] and (
            len(design) == len(towel) or add_towel(design[len(towel):])
        )
        for towel in towels
    )

for design in designs:
    result += add_towel(design)

print(result)
submit(result)