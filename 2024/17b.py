from aocd import submit, data
import re

program = list(map(int, re.findall(r"\d+", data)))[3:]

solutions = [set() for _ in range(len(program)+1)]
solutions[0].add(0) # initial value 0

for i, p in enumerate(reversed(program)): # solve reversed output by output 
    i+=1
    for s in solutions[i-1]:    # expand previous solutions by 3 bits or 8 possibilities
        for a in range(8):      # so the program produces one more output  
            A = s*8 + a
            # run one iteration of program (up to the jump) 3(0)
            B = (A%8) ^ 1           # 2(4=A), 1(1)
            C = A//(2**B)           # 7(5=B)
            if ((B^5)^C)%8 == p:    # 1(5), 4(), 5(5=B)
                solutions[i].add(A)

    print(i+1,': ', solutions[i])

print(min(solutions[-1])) # select lowest solution
submit(min(solutions[-1]))
