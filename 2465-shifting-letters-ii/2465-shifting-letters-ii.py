class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        
        # Step 1: Create a `moves` array to track the net shifts at each position
        moves = [0] * (n + 1)  # One extra space for handling boundaries

        # Step 2: Update the `moves` array for each shift operation
        for start, end, direction in shifts:
            if direction == 1:  # Forward shift
                moves[start] += 1
                moves[end + 1] -= 1
            else:  # Backward shift
                moves[start] -= 1
                moves[end + 1] += 1
        
        # Step 3: Compute the prefix sum to determine the final shifts for each character
        for i in range(1, n):
            moves[i] += moves[i - 1]
        
        # Step 4: Apply the shifts to the string `s` and construct the result
        result = []
        for i in range(n):
            shift = (ord(s[i]) - ord('a') + moves[i]) % 26
            result.append(chr(ord('a') + shift))
        
        return ''.join(result)
