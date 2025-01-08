class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(str1, str2):
            k = len(str1)
            m = len(str2)

            if k > m :
                return 0
            return str1 == str2[:k] == str2[-k:]

        n = len(words)
        count = 0
        for i in range(n):
            word1 = words[i]
            for j in range(i+1,n):
                word2 = words[j]
                count += isPrefixAndSuffix(word1, word2)
        return count
            
