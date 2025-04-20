# Test in a separate file or console
from disjoint_set import DisjointSet
ds = DisjointSet(5)
print(ds.union(0, 1))  # True
print(ds.union(1, 2))  # True
print(ds.union(0, 2))  # False