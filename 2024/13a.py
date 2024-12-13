from aocd import data, submit
from pulp import LpMinimize, LpProblem, LpVariable, LpInteger, value
import re

result = 0
data = data.split("\n\n")
eqs = [tuple(map(int, re.findall(r"\d+", problem))) for problem in data]

prob = LpProblem("Minimize_3a+b", LpMinimize)
a = LpVariable("a", lowBound=0, upBound=100, cat=LpInteger)  
b = LpVariable("b", lowBound=0, upBound=100, cat=LpInteger)
prob += 3*a + b, "Objective Function"

for eq in eqs:
    prob += eq[0]*a + eq[2]*b == eq[4]
    prob += eq[1]*a + eq[3]*b == eq[5]
    status = prob.solve()
    if status == 1:
        result += value(prob.objective)
    prob.constraints.clear()

submit(result)