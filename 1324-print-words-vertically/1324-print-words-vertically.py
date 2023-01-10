class Solution:
    def printVertically(self, s: str) -> List[str]:
        result_array = list(s.split())
        max_length = len(result_array[0])
        for word in result_array:
            max_length = max(max_length, len(word))
        vertical_words =[]
        for index in range(max_length):
            temp_word = ''
            for word in result_array:
                if len(word)> index:
                    temp_word += word[index]
                else:
                    temp_word += " "
            vertical_words.append(temp_word)
        for index in range(len(vertical_words)):
            vertical_words[index] = vertical_words[index].rstrip()
        return vertical_words
            
            