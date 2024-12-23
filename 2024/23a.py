from aocd import data, submit
import networkx as nx

nodes = data.splitlines() # Split the string into lines

G = nx.Graph()
for node in nodes:
    a, b = node.split('-')
    G.add_edge(a, b)

triangles = [list(triangle) for triangle in nx.enumerate_all_cliques(G) if len(triangle) == 3]

# Filter for 't' nodes
triangles = [triangle for triangle in triangles if any(node.startswith('t') for node in triangle)]

print(len(triangles))
submit(len(triangles))