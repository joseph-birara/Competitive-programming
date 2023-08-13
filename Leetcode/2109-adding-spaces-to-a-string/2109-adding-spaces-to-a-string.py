class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        newArray =[]
        indexIncrement =0
        startIndex =0
        for index in spaces:
            stringPart = s[startIndex:index+indexIncrement] + " "
            startIndex = index+indexIncrement
            newArray.append(stringPart)
        newArray.append(s[ startIndex:])
        
        return  ''.join(newArray)
        
        