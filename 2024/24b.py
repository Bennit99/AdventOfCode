from aocd import data, submit
from collections import Counter

data, operations = data.split("\n\n")
data = {x.split(": ")[0]: bool(int(x.split(": ")[1])) for x in data.splitlines()} # Parse data into dictionary
operations = [x.split(" ") for x in operations.splitlines()]

# Count occurrences of variable names
var_counts = Counter()
for x, _, y, _, _ in operations:
    var_counts[x] += 1
    var_counts[y] += 1

sus = []                        # find sus gates
for _, op, _, _, z in operations:
    if z[0] == "z":             # Output variable are produced by XOR (except for last one: z45)
        if op != 'XOR' and z != 'z45':
            sus.append(z)
        continue
    if op == "AND":             # AND gates outputs are connected to a single or
        if var_counts[z] != 1:
            sus.append(z)
    elif var_counts[z] != 2:    # other gates outputs are connected to two further gates
        sus.append(z)

sus.remove('nqp')               # manual analyse (nqp is special case of first carry)
sus.append('gmh')               # z13 needs to be swapped with gmh
sus.sort()
result = ",".join(sus)
print(result)
submit(result)
