class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def computeLPS(pattern):
            n = len(pattern)
            lps = [0] * n
            length = 0
            i = 1

            while i < n:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1

            return lps

        if not s:
            return ""

        rev_s = s[::-1]
        concat = s + "#" + rev_s
        lps = computeLPS(concat)

        palindrome_prefix_length = lps[-1]
        suffix = s[palindrome_prefix_length:]

        return suffix[::-1] + s