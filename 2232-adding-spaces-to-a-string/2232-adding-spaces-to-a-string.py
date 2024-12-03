class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        newstr = ''
        k = 0
        n = len(spaces)

        for index, char in enumerate(s):
            print(index, k, newstr)
            if k < n and index == spaces[k]:
                newstr += ' ' 
                k += 1
            newstr += char
        return newstr 
            

        