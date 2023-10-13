class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        n = len(word)
        temp = ''
        word_list = []


        for i in range(n):
            if 'A' <= word[i] <='z':
                if temp:
                    word_list.append(temp)
                temp = ''
            else:
                temp +=word[i]
        if temp:
            word_list.append(temp)
        for i in range(len(word_list)):
            word_list[i] = int(word_list[i])
        # print(word_list)
        
        
        return len(Counter(word_list))
        