
class TrieNode:
    def __init__(self):
        self.child = {}
        self.val = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self,word):
        curr = self.root
        for c in word:
            curr = curr.child.setdefault(c,TrieNode())
            curr.val +=1
               
    def search(self, word):
        curr = self.root  
        res = 0  
        for c in word:
            curr = curr.child[c]
            res+=curr.val
        return res


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie()
        ans = []
        for word in words:
            root.addWord(word)
        for word in words:
            ans.append(root.search(word))
        return ans


        