class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        currentHash = 0
        startIdx = -1
        powerK = (power ** k) % modulo

        i = len(s) - 1
        while i >= 0:
            currentHash = (currentHash * power + ord(s[i]) - ord('a') + 1) % modulo

            if i + k < len(s):
                currentHash = (currentHash - (ord(s[i + k]) - ord('a') + 1) * powerK) % modulo

            if currentHash == hashValue:
                startIdx = i

            i -= 1

        if startIdx != -1:
            return s[startIdx:startIdx + k]
        else:
            return ""
