class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        
        ans = set()


        for index,word in enumerate(words):
            for i,word2 in enumerate(words):
                if i != index and word in word2:
                    ans.add(word)
                    break

        return list(ans)
        