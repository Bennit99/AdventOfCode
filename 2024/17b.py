from aocd import data, submit
import re
import time

result = 0
data = list(map(int, re.findall(r"\d+", data)))
A_counter = 0
program = data[3:]

# opcodes 
# 0
def adv(A, operand, B):
    denominator = 2 ** (operand if operand < 5 else B)
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
    denominator = 2 ** (operand if operand < 5 else B)
    return A // denominator

# 7
def cdv(A, operand, B):
    denominator = 2 ** (operand if operand < 5 else B)
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

start = time.time()
record = 0

while True:
    output = []
    instruction_pointer = 0
    A = A_counter
    B = data[1]
    C = data[2]
    while instruction_pointer < len(program):
        prev = A, B, C, instruction_pointer # Save the state of the program for loop detection
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
            output.append(out(combo(operand)))
        elif opcode == 6:
            B = bdv(A, combo(operand), B)
        elif opcode == 7:
            C = cdv(A, combo(operand), B)
        instruction_pointer += 2
        if output != program[:len(output)]:
            break
        # log the record of the longest output
        if len(output) >= record:
            record = len(output)
            print(f"Record: {record}, A_counter: {A_counter}")
        if prev == (A, B, C, instruction_pointer): # Loop detected
            print('Loop detected')
            break
    if output == program:
        result = A_counter
        break
    A_counter += 1

    # logging
    if A_counter % 1000000 == 0:
        print(f"A_counter: {A_counter}, Time elapsed: {(time.time() - start)/60:.2f} minutes")

print(result)
# submit(result)