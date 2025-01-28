class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        
        # Left-to-right pass
        moves = 0
        count = 0
        for i in range(n):
            ans[i] += moves
            count += int(boxes[i])  # Add current box to ball count if it has a ball
            moves += count  # Update moves based on current count

        # Right-to-left pass
        moves = 0
        count = 0
        for i in range(n - 1, -1, -1):
            ans[i] += moves
            count += int(boxes[i])  # Add current box to ball count if it has a ball
            moves += count  # Update moves based on current count
        
        return ans
