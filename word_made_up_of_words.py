class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:            
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True
    def search(self,word):
        node = self.root
        for c in word:
            if c in node.children and node.children[c].isWord:
                node = node.children[c]
            else:
                return False
        return True        

        

   

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()
        for word in words:
            root.insert(word)
        res =''
        for word in words:
            if root.search(word):
                if not res:
                    res = word
                else:
                    if len(res)< len(word):
                        res = word
                    elif len(res)== len(word):
                        if res > word:
                            res = word
        return res

        


        
