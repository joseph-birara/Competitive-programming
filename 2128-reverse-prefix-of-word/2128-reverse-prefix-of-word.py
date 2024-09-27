class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the index of the first occurrence of 'ch'
        index = word.find(ch)
        
        # If 'ch' is found, reverse the segment from 0 to the found index
        if index != -1:
            return word[:index + 1][::-1] + word[index + 1:]
        
        # If 'ch' is not found, return the word as is
        return word
 