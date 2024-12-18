from aocd import data, submit
import re

result = ''
data = list(map(int, re.findall(r"\d+", data)))
A = 10001101110 # data[0]
B = 0 # data[1]
C = 0 # data[2]

program = data[3:]
instruction_pointer = 0

# opcodes 
# 0
def adv(A, operand, B):
    denominator = 2 ** operand
    return A // denominator

# 1
def bxl(B, operand):
    return B ^ operand

# 2
def bst(operand):
    return operand % 8

# 3
def jnz(A, operand, instruction_pointer):
    if A != 0:
        return operand
    return instruction_pointer + 2

# 4
def bxc(B, C):
    return B ^ C

# 5
def out(operand):
    return operand % 8

# 6
def bdv(A, operand, B):
    denominator = 2 ** operand
    return A // denominator

# 7
def cdv(A, operand, B):
    denominator = 2 ** operand
    return A // denominator

def combo(operand):
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    if operand == 7:
        print('invalid operand')
        return
    return operand

while instruction_pointer < len(program):
    opcode = program[instruction_pointer]
    operand = program[instruction_pointer + 1]

    if opcode == 0:
        A = adv(A, combo(operand), B)
    elif opcode == 1:
        B = bxl(B, operand)
    elif opcode == 2:
        B = bst(combo(operand))
    elif opcode == 3:
        instruction_pointer = jnz(A, operand, instruction_pointer)
        continue  # Skip the increment of instruction_pointer
    elif opcode == 4:
        B = bxc(B, C)
    elif opcode == 5:
        result += str(out(combo(operand))) + ','
    elif opcode == 6:
        B = bdv(A, combo(operand), B)
    elif opcode == 7:
        C = cdv(A, combo(operand), B)
    instruction_pointer += 2

# Remove the trailing comma from the result
result = result.rstrip(',')

print(result)
submit(result)