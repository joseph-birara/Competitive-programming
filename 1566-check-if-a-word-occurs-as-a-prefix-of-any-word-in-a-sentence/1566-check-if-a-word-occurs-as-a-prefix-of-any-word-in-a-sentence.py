class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Split the sentence into words
        words = sentence.split()
        
        # Iterate through the words with their 1-based indices
        for index, word in enumerate(words, start=1):
            if word.startswith(searchWord):
                return index
        
        # If no word matches, return -1
        return -1
