class DisjointSet:
    # Manages sets of cells to ensure the formation of a spanning tree (no cycles)
    def __init__(self, size):
        # Each cell starts as its own set -> parent[i] = i
        self.parent = list(range(size))
        # Tracks tree height
        self.rank = [0] * size
        
    # Find locates the root of a cell's set
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    # Union function merges two sets if they are unconnected using rank
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True
    
    