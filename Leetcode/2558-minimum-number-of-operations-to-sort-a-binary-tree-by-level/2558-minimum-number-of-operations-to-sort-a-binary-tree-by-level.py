from collections import deque

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def minSwapsToSort(arr):
            n = len(arr)
            sorted_arr = sorted([(val, i) for i, val in enumerate(arr)])  # Pair values with original indices
            visited = [False] * n  # Mark visited indices
            swaps = 0
            
            for i in range(n):
                if visited[i] or sorted_arr[i][1] == i:
                    continue
                
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = sorted_arr[j][1]
                    cycle_size += 1
                
                if cycle_size > 1:
                    swaps += cycle_size - 1
            
            return swaps

        if not root:
            return 0

        queue = deque([root])
        total_swaps = 0

        while queue:
            level_size = len(queue)
            level_values = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Count the swaps needed for this level
            total_swaps += minSwapsToSort(level_values)
        
        return total_swaps
