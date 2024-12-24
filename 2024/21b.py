from aocd import data, submit
from functools import cache

result = 0
codes = data.splitlines() # Split the string into lines

num_keypad = {
    '7': (0,0),
    '8': (0,1),
    '9': (0,2),
    '4': (1,0),   
    '5': (1,1),
    '6': (1,2),
    '1': (2,0),
    '2': (2,1),
    '3': (2,2),  
    '0': (3,1),
    'A': (3,2)
}

dir_keypad = {
    '^': (0,1),
    'A': (0,2),
    '<': (1,0),
    'v': (1,1),
    '>': (1,2)
}

@cache
def calculate_snipped(code):
    result =[]
    pos = (0,2)
    for move in code:
        next_pos = dir_keypad[move]
        dr, dc = next_pos[0] - pos[0], next_pos[1] - pos[1]
        next_code = ''
        if (pos[0], next_pos[1]) == (0,0):
            next_code += 'v' * dr + '<' * -dc
        elif (next_pos[0], pos[1]) == (0,0):
            next_code += '>' * dc + '^' * -dr
        else:
            next_code += '<'*-dc + 'v'*dr + '^'*-dr + '>'*dc
        result.append(next_code + 'A')
        pos = next_pos
    return result

@cache
def recursive_solve(code, step=0):
    if step == 25:
        return len(code)
    next_code = calculate_snipped(code)
    return sum(recursive_solve(c, step+1) for c in next_code)

for code in codes:
    og_code = code
    # numeric keypad
    pos = (3, 2)
    illegal_position = (3, 0)
    code_list = []
    for char in code:
        next_code = ''
        next_pos = num_keypad[char]
        dr, dc = next_pos[0] - pos[0], next_pos[1] - pos[1]
        if (pos[0], next_pos[1]) == illegal_position:
            next_code += '^' * -dr + '<' * -dc
        elif (next_pos[0], pos[1]) == illegal_position:
            next_code += '>' * dc + 'v' * dr
        else:
            next_code += '<'*-dc + 'v'*dr + '^'*-dr + '>'*dc
        next_code += 'A'
        code_list.append(next_code)
        pos = next_pos

    code_len = sum(recursive_solve(c) for c in code_list)

    result += code_len*int(og_code[:-1])

print(result)
submit(result)