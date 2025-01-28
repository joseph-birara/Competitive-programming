class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        m = len(queries)
        prefix = [0]*n
        vowels = ['a','e','u','i','o']

        def isTrue(word):
            return int(word[0] in vowels and word[-1] in vowels)

        for i, word in enumerate(words):
            prefix[i] = prefix[i-1] + isTrue(word) if i > 0 else isTrue(word)
        
        ans = []
        for a,b in queries :
            count = prefix[b]
            if a > 0:
                count -= prefix[a-1]
            ans.append(count)
        return ans