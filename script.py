from __future__ import annotations
from data import create_as, create_bs
from graph import subgraphs_of_size_two, vert_of_degree


ws = create_as()
bs = create_bs()

print("matches one-to-one")
for w, b in subgraphs_of_size_two(ws, bs):
    print(f"{w} <-> {b}")

print()
print("white degree zero vertices")
print(vert_of_degree(0, ws, bs))
print()
print("black degree zero vertices")
print(vert_of_degree(0, bs, ws))
