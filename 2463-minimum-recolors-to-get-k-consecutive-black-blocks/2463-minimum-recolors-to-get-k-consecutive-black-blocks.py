class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        min_operations = float('inf')
        white_count = 0

        for i in range(len(blocks)):
            if blocks[i] == 'W':
                white_count += 1

            if i >= k - 1:
                min_operations = min(min_operations, white_count)
                if blocks[i - k + 1] == 'W':
                    white_count -= 1

        return min_operations

        