from collections import defaultdict

class Solution:
    def sortVowels(self, s: str) -> str:

        t = ''
        d = defaultdict(int)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels.sort()
        i = 0
        for ele in s:
            if ele in vowels:
                d[ele] += 1

        for ele in s:
            if ele in vowels:
                for vo in vowels:
                    if d[vo]:
                        d[vo] -= 1
                        t += vo
                        break
            else:
                t += ele
        return t
