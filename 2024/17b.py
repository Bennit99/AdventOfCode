from aocd import data, submit
import re

result = 0
data = list(map(int, re.findall(r"\d+", data)))
program = data[3:]
B = data[1]
C = data[2]

def combo(operand, A, B, C):
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    return operand

solutions = [set() for _ in range(len(program))]

def check(s, i, digits, C=C, B=B, program=program):
    for counter in range(0, 2**digits):
        A = counter*(2**len(s)) + int(s, 2)
        if A < 2**43:
            A += 2**43
        A_innit = A
        output = []
        instruction_pointer = 0
        relevant_digits = 3 
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
                output.append(combo(operand, A, B, C) % 8)
                if output != program[:len(output)]:
                    break
                else:
                    if len(output) == i+1:
                        x = bin(A)
                        y = str(x)
                        z = y[-relevant_digits:]
                        possible = str(bin(A_innit))[-relevant_digits:]
                        if possible not in solutions[i]:
                            print(i+1,': ', possible)
                            solutions[i].add(possible)
            elif opcode == 6:
                B = A // (2 ** combo(operand, A, B, C))
            elif opcode == 7:
                C = A // (2 ** combo(operand, A, B, C))
                relevant_digits = B+(3*(i+1))
            instruction_pointer += 2

        if output == program:
            result = A_innit
            print(result)
            submit(result)
            break


for i in range(0, len(program)):
    if i == 0: # innit
        check('0', i, 10)
    for s in solutions[i-1]:
        digits = 10 + i*3 - len(s)
        check(s, i, digits)
    print('Solutions: ', len(solutions[i]))

