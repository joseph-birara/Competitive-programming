class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        n = len(A)
        C = [0] * n
        hashA = defaultdict(int)
        

        for i in range(n):
            hashA[A[i]] += 1
            cnt = 0
            for i in range(i+1):
                if hashA[B[i]]:
                    cnt += 1
            
            C[i] = cnt

        return C

            

        