class Solution:
    def _is_vowel(self, c: str) -> bool:
        return c in "aeiou"

    def countOfSubstrings(self, s: str, k: int) -> int:
        count = 0
        l = r = 0
        v_count = {}
        c_count = 0
        nxt_c = [0] * len(s)
        nxt_c_idx = len(s)

        for i in range(len(s) - 1, -1, -1):
            nxt_c[i] = nxt_c_idx
            if not self._is_vowel(s[i]):
                nxt_c_idx = i

        while r < len(s):
            if self._is_vowel(s[r]):
                v_count[s[r]] = v_count.get(s[r], 0) + 1
            else:
                c_count += 1

            while c_count > k:
                if self._is_vowel(s[l]):
                    v_count[s[l]] -= 1
                    if v_count[s[l]] == 0:
                        del v_count[s[l]]
                else:
                    c_count -= 1
                l += 1

            while l < len(s) and len(v_count) == 5 and c_count == k:
                count += nxt_c[r] - r
                if self._is_vowel(s[l]):
                    v_count[s[l]] -= 1
                    if v_count[s[l]] == 0:
                        del v_count[s[l]]
                else:
                    c_count -= 1
                l += 1

            r += 1

        return count
