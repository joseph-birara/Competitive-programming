class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            count = 0
            for char in counter:
                if counter[char] > 0:
                    count += 1  
                    counter[char] -= 1  
                    count += backtrack(counter)  
                    counter[char] += 1
            return count
        
        counter = Counter(tiles)
        return backtrack(counter)
        