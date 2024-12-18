program = [2, 4, 1, 1, 7, 5, 1, 5, 4, 2, 5, 5, 0, 3, 3, 0]

def combo(operand, A, B, C):
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    return operand

instruction_pointer = 0
A = 164278496489149
B = 0
C = 0
while instruction_pointer < len(program):
    opcode = program[instruction_pointer]
    operand = program[instruction_pointer + 1]

    if opcode == 0:
        A = A // (2 ** combo(operand, A, B, C))
    elif opcode == 1:
        B = B ^ operand
    elif opcode == 2:
        B = combo(operand, A, B, C) % 8
    elif opcode == 3:
        if A != 0:
            instruction_pointer = operand
        else:
            instruction_pointer += 2
        continue  # Skip the increment of instruction_pointer
    elif opcode == 4:
        B = B ^ C
    elif opcode == 5:
        print(combo(operand, A, B, C) % 8)
    elif opcode == 6:
        B = A // (2 ** combo(operand, A, B, C))
    elif opcode == 7:
        C = A // (2 ** combo(operand, A, B, C))
    instruction_pointer += 2