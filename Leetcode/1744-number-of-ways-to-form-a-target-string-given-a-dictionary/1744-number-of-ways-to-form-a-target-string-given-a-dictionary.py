class Solution:
    def numWays(self, words, target):
        m, n = len(words[0]), len(target)
        
        # Precompute the frequency of each character at every column.
        char_count = [[0] * 26 for _ in range(m)]
        for word in words:
            for col, char in enumerate(word):
                char_count[col][ord(char) - ord('a')] += 1

        # Memoization table initialized with -1.
        dp = [[-1] * n for _ in range(m)]

        def dfs(word_col, target_idx):
            # If we've matched all of target, there's 1 way.
            if target_idx == n:
                return 1
            # If we're out of columns or not enough columns remain, no ways.
            if word_col == m or m - word_col < n - target_idx:
                return 0
            # If already computed, return cached result.
            if dp[word_col][target_idx] != -1:
                return dp[word_col][target_idx]
            
            ways = dfs(word_col + 1, target_idx)  # Skip this column.
            char = target[target_idx]
            char_idx = ord(char) - ord('a')
            # Use this column if it has the required character.
            if char_count[word_col][char_idx] > 0:
                ways += char_count[word_col][char_idx] * dfs(word_col + 1, target_idx + 1)
            
            dp[word_col][target_idx] = ways % 1_000_000_007
            return dp[word_col][target_idx]

        return dfs(0, 0)
