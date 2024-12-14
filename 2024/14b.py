from aocd import data, submit
import re
import matplotlib.pyplot as plt
import numpy as np
import os

result = 0
data = data.split("\n")
robots = [list(map(int, re.findall(r"-?\d+", problem))) for problem in data]

r_len = 103
c_len = 101 
iterations = 10000  # try and error

'''-----Variant A-----'''
# use the security score from part 1
security_scores = []
for i in range(iterations):
    quadrants = [0, 0, 0, 0]
    for robot in robots:                    # calculate ech robot severalty
        c, r, cv, rv = robot
        r = (r + rv + r_len) % r_len
        c = (c + cv + c_len) % c_len
        robot[0] = c
        robot[1] = r
        if r == r_len//2 or c == c_len//2:  # ignore the center lines
            continue
        q = 0 if r < r_len // 2 else 1
        q += 0 if c < c_len // 2 else 2
        quadrants[q] += 1
    security_scores.append(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])

tree = security_scores.index(min(security_scores)) + 1
# plot distribution of security scores
plt.plot(security_scores)
plt.show()
print(tree)
submit(tree)

'''-----Variant B-----'''
# create a image for every second 
# sort images by size in explorer 
# smallest one is the chrisms tree
for second in range(iterations):
    room = np.ones((r_len, c_len, 3), dtype=int) * 255  # White pixels
    for robot in robots:
        c, r, cv, rv = robot
        r = (r + rv + r_len) % r_len
        c = (c + cv + c_len) % c_len
        room[r][c] = [0, 0, 0]  # black pixel
        robot[0] = c
        robot[1] = r
    
    plt.imshow(room, interpolation='nearest')
    plt.axis('off')  # Turn off the axis
    
    # Save the plot to the specified folder
    plt.savefig(os.path.join('./robots/', f"{second}.png"), bbox_inches='tight', pad_inches=0)
    plt.close()  # Close the plot to free memory

# shortcut
# horizontal and vertical anomalies in regular intervals
# horizontal every: 28 + 101*x
# vertical every: 86 + 103*y
# they meet at Tree location at 7502 = 28 + 101*74 = 86 + 103*72 
    
