from aocd import data, submit
import networkx as nx

result = ''
nodes = data.splitlines() # Split the string into lines

G = nx.Graph()
for node in nodes:
    a, b = node.split('-')
    G.add_edge(a, b)

# Find all cliques
cliques = list(nx.find_cliques(G))

# Find the largest clique
largest_clique = max(cliques, key=len)

computer = set()
for node in largest_clique:
    computer.add(node)

sorted_computer = sorted(computer)
for node in sorted_computer:
    result += node + ','

result = result[:-1]

print(result)
submit(result)