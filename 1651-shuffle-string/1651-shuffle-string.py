class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        shufled = [0]* n

        for index, value in enumerate(indices):
            
            shufled[value] = s[index]
        
        return ''.join(shufled)

        