from typing import List
from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Step 1: Build adjacency list for the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Step 2: Find the path from Bob's starting node to root (0)
        bob_time = {}  # Stores when Bob reaches each node
        def find_bob_path(node, parent, time):
            if node == 0:
                bob_time[node] = time
                return True
            found = False
            for neighbor in tree[node]:
                if neighbor != parent:
                    if find_bob_path(neighbor, node, time + 1):
                        bob_time[node] = time
                        found = True
            return found
        find_bob_path(bob, -1, 0)

        # Step 3: DFS to calculate Alice’s best possible profit
        max_profit = float('-inf')
        def dfs_alice(node, parent, time, current_profit):
            nonlocal max_profit
            
            # Step 4: Adjust profit considering Bob's presence
            if node in bob_time:
                if time < bob_time[node]:  # Alice reaches first
                    current_profit += amount[node]
                elif time == bob_time[node]:  # Both reach simultaneously
                    current_profit += amount[node] // 2
            else:  # Alice reaches first or Bob never reaches
                current_profit += amount[node]

            # Check if it's a leaf node (except root)
            is_leaf = True
            for neighbor in tree[node]:
                if neighbor != parent:
                    is_leaf = False
                    dfs_alice(neighbor, node, time + 1, current_profit)
            
            if is_leaf:  # Update max profit at leaf nodes
                max_profit = max(max_profit, current_profit)
        
        dfs_alice(0, -1, 0, 0)
        return max_profit
