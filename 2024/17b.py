from aocd import data, submit
import re
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

def combo(operand, A, B, C):
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    return operand

def process_chunk(start_counter, end_counter, B, C, program):
    for A_counter in range(start_counter, end_counter):
        output = []
        instruction_pointer = 0
        A = A_counter
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
            elif opcode == 6:
                B = A // (2 ** combo(operand, A, B, C))
            elif opcode == 7:
                C = A // (2 ** combo(operand, A, B, C))
            instruction_pointer += 2

        if output == program:
            return A_counter
    return None

if __name__ == '__main__':
    result = 0
    data = list(map(int, re.findall(r"\d+", data)))
    program = data[3:]
    B = data[1]
    C = data[2]

    start = time.time()
    record = 0
    chunk_size = 10000000
    num_workers = 1

    start_counter = 1000000000000000000000000000000000000000000

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(process_chunk, i, i + chunk_size, B, C, program) for i in range(start_counter, start_counter + chunk_size * num_workers, chunk_size)]
        start_counter += chunk_size * (num_workers-1)

        found = False
        while not found:
            for future in as_completed(futures):
                result = future.result()
                if result is not None:
                    print(result)
                    # submit(result)
                    found = True
                    break
                # Submit a new task to keep the search going
                start_counter += chunk_size
                print(f"A_counter: {start_counter} Time elapsed: {(time.time() - start)/60:.2f} minutes")
                futures.append(executor.submit(process_chunk, start_counter, start_counter + chunk_size, B, C, program))
            

