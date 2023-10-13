class TrieNode:
    def __init__ (self):
        self.children = {}
        self.val = 0

class Trie:
    def __init__ (self):
        self.root = TrieNode()        
    def addWord(self,word,val):
        curr = self.root
        for c in word:
            curr = curr.children.setdefault(c,TrieNode())
            curr.val +=val
    def sum_prefix(self,prefix):
        res = 0
        curr = self.root
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return 0
        res+= curr.val
        return res
        
class MapSum:

    def __init__(self):
        self.hashMap = defaultdict(int)
        self.trie = Trie()       

    def insert(self, key: str, val: int) -> None:
        root = self.trie
        if key in self.hashMap:
            temp  = val
            val =  val -self.hashMap[key]
            self.hashMap[key] = temp

        else:
            self.hashMap[key] = val
        root.addWord(key,val)                

    def sum(self, prefix: str) -> int:
        root = self.trie
        return root.sum_prefix(prefix)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
