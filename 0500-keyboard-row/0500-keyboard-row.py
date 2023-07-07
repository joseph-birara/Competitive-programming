

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []
        
        for word in words:
            for row in rows:
                if all(ch.lower() in row for ch in word):
                    result.append(word)
                    break
                    
        return result
      

                    
                

        