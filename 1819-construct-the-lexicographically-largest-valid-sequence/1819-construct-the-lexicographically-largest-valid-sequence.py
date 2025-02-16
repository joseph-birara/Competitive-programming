class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1  # Length of the sequence
        sequence = [0] * size  # Initialize with zeros
        used = [False] * (n + 1)  # Track used numbers
        
        def backtrack(index):
            if index == size:  # Base case: all positions filled
                return True
            
            if sequence[index] != 0:  # Skip filled positions
                return backtrack(index + 1)
            
            # Try placing numbers from largest to smallest
            for num in range(n, 1, -1):
                if used[num]:  # Skip if already used
                    continue
                
                # Check if placement is valid
                if index + num < size and sequence[index] == 0 and sequence[index + num] == 0:
                    # Place the number
                    sequence[index] = sequence[index + num] = num
                    used[num] = True
                    
                    # Recur to place the next number
                    if backtrack(index + 1):
                        return True
                    
                    # Undo the placement
                    sequence[index] = sequence[index + num] = 0
                    used[num] = False
            
            # Place `1` (since it appears only once)
            if not used[1]:
                sequence[index] = 1
                used[1] = True
                if backtrack(index + 1):
                    return True
                sequence[index] = 0
                used[1] = False
            
            return False
        
        backtrack(0)
        return sequence

            
    

            