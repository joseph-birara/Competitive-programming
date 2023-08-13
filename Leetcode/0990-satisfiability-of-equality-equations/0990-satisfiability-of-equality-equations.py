class DisjointSetUnion:
    def __init__(self):
        self.rank = [0] * 26  # Initialize ranks for 26 characters ('a' to 'z')
        self.parent = [i for i in range(26)]  # Initialize parent array for 26 characters

    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])  # Path compression while finding
        return self.parent[node]

    def union_by_rank(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1


class Solution:
    def equationsPossible(self, equations):
        disjoint_set = DisjointSetUnion()
        not_equal_equations = []

        for equation in equations:
            if equation[1] == '!':
                if equation[0] == equation[-1]:  # A variable is not equal to itself, contradiction
                    return False
                else:
                    not_equal_equations.append(equation)
            else:
                char_x, char_y = equation[0], equation[-1]
                x, y = ord(char_x) - 97, ord(char_y) - 97  # Convert characters to integers (0 to 25)
                disjoint_set.union_by_rank(x, y)

        for equation in not_equal_equations:
            char_x, char_y = equation[0], equation[-1]
            x, y = ord(char_x) - 97, ord(char_y) - 97
            if disjoint_set.find(x) == disjoint_set.find(y):  # Check for contradiction
                return False

        return True
