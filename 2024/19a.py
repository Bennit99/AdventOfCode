from aocd import data, submit

result = 0
towels, designs = data.split("\n\n")
towels = towels.split(", ")
designs = designs.split("\n")

def add_towel(design):
    return any(
        towel == design[:len(towel)] and (
            len(design) == len(towel) or add_towel(design[len(towel):])
        )
        for towel in towels
    )

for design in designs:
    if add_towel(design):
        result += 1

print(result)
submit(result)