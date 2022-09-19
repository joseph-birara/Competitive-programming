class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        q = collections.deque()
        q.append((beginWord, 1))
        lngth = len(beginWord)
        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            for i in range(lngth):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    res = word[:i]+c+word[i+1:]
                    if res in wordset:
                        wordset.remove(res)
                        q.append((res, step+1))
        return 0
        