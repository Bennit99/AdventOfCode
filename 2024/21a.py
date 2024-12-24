from aocd import data, submit

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

for code in codes:
    og_code = code
    print(code)
    pos = (3, 2)
    keypad = num_keypad
    illegal_position = (3, 0)
    for _ in range(3):
        next_code = ''
        for char in code:
            next_pos = keypad[char]
            dr, dc = next_pos[0] - pos[0], next_pos[1] - pos[1]
            if (pos[0], next_pos[1]) == illegal_position:
                next_code += '^' * -dr + '<' * -dc
            elif (next_pos[0], pos[1]) == illegal_position:
                next_code += '>' * dc + 'v' * dr
            else:
                next_code += '<' * -dc + 'v' * dr + '^' * -dr + '>' * dc
            next_code += 'A'
            pos = next_pos
            code = next_code
        print(code)
        pos = (0,2)
        keypad = dir_keypad
    print(len(code))
    result += len(code)*int(og_code[:-1])

print(result)
submit(result)