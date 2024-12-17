program = [2, 4, 1, 1, 7, 5, 1, 5, 4, 2, 5, 5, 0, 3, 3, 0]

def combo(operand, A, B, C):
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    return operand

solutions = [set() for _ in range(len(program) + 1)]
solutions[0].add(4)

for i, p in enumerate(reversed(program[:-1])):
    i+=1
    for s in solutions[i-1]:
        for a in range(0, 2**3):
            a = s*(2**(i*3)) + a
            instruction_pointer = 0git 
            A = a
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
                    break
                    if A != 0:
                        instruction_pointer = operand
                    else:
                        instruction_pointer += 2
                    continue  # Skip the increment of instruction_pointer
                elif opcode == 4:
                    B = B ^ C
                elif opcode == 5:
                    if(combo(operand, A, B, C) % 8) == p:
                        solutions[i].add(a)
                elif opcode == 6:
                    B = A // (2 ** combo(operand, A, B, C))
                elif opcode == 7:
                    C = A // (2 ** combo(operand, A, B, C))
                instruction_pointer += 2
    print(i+1,': ', solutions[i])