from typing import List

class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = {}
            self.size = {}

        def find(self, x):
            if x not in self.parent:
                self.parent[x] = x
                self.size[x] = 1
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])  # Path compression
            return self.parent[x]

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x != root_y:
                if self.size[root_x] >= self.size[root_y]:
                    self.parent[root_y] = root_x
                    self.size[root_x] += self.size[root_y]
                else:
                    self.parent[root_x] = root_y
                    self.size[root_y] += self.size[root_x]

    def removeStones(self, stones: List[List[int]]) -> int:
        uf = self.UnionFind()

        for x, y in stones:
            uf.union(x, ~y)  # Connect elements of the same row and column

        # Calculate the number of stones that can be removed
        removed_stones = len(stones) - len({uf.find(x) for x, y in stones})
        return removed_stones
