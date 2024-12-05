class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Remove blanks and compare the sequences of 'L' and 'R'
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        # Two pointers to compare positions of 'L' and 'R'
        i, j = 0, 0
        n = len(start)
        
        while i < n and j < n:
            # Skip blanks in both strings
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            
            # If we reached the end of either string, break
            if i == n or j == n:
                break
            
            # Check movement constraints for 'L' and 'R'
            if start[i] != target[j]:
                return False
            if start[i] == 'L' and i < j:  # 'L' can't move right
                return False
            if start[i] == 'R' and i > j:  # 'R' can't move left
                return False
            
            # Move both pointers
            i += 1
            j += 1
        
        # Ensure all remaining characters in both strings are blanks
        while i < n:
            if start[i] != '_':
                return False
            i += 1
        while j < n:
            if target[j] != '_':
                return False
            j += 1
        
        return True
