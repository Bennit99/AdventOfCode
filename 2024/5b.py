from aocd import data, submit

result = 0

# Split the string into lines
data = data.splitlines()

# Split the lines into two parts
rules = data[:data.index('')]
updates = data[data.index('')+1:]

# Split each line by the delimiter and convert to a list of lists
rules = [list(map(int, line.split('|'))) for line in rules]
updates = [list(map(int, line.split(','))) for line in updates]

for update in updates:  # go through update list
    changed = False
    while True:
        for a, b in rules:  # check rules
            if a in update and b in update and update.index(a) > update.index(b):  # rule is violated
                update.insert(update.index(b), update.pop(update.index(a)))  # reorder value b
                changed = True
                break
        else: 
            break  # no rule is violated
    if not changed:  # if no changes were made
        update[(len(update) // 2)] = 0  # this update is correct -> set the middle value to 0

# sum up the middle values of the lists in u
result = sum(update[len(update) // 2] for update in updates)

submit(result)