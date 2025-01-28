class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Store indices of each character in a defaultdict
        char_indices = defaultdict(list)

        for index, letter in enumerate(s):
            char_indices[letter].append(index)
        
        count = 0

        for char, indices in char_indices.items():
            if len(indices) > 1:
                # Find the first and last occurrence
                left, right = indices[0], indices[-1]

                # Use a set for unique characters in the middle
                unique_chars = set(s[left+1:right])
                count += len(unique_chars)
        
        return count
