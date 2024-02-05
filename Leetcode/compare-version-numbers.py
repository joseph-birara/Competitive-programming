class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n , m = len(v1), len(v2)

        for i in range(n,m):
            v1.append('0')
        for j in range(m,n):
            v2.append('0')
        n , m = len(v1), len(v2)

        for i in range(n):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        return 0

        


        