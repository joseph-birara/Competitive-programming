

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        hashmap = defaultdict(int)
        n = len(path)
        curr_n, curr_e = 0, 0
        hashmap[(0,0)] = 1

        for i in range(n):
            if path[i] == 'N':
                curr_n += 1
            elif path[i] == 'E':
                curr_e += 1
            elif path[i] == 'W':
                curr_e -= 1
            else:
                curr_n -= 1

           
            if (curr_e, curr_n) in hashmap :
                return True

            hashmap[(curr_e, curr_n)] += 1

        return False


