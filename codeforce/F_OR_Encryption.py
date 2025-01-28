# It gives you a table M
#  with n
#  rows and n
#  columns of non-negative integers, and to open the lock, you need to find an array a
#  of n
#  elements such that:

# 0≤ai<230
# , and
# Mi,j=ai|aj
#  for all i≠j
# , where |
#  denotes the bitwise OR operation.
# The lock has a bug, and sometimes it gives tables without any solutions. In that case, the ice cream will remain frozen for the rest of eternity.


#reurn a

def find_a():
    n = int(input())
    M = []
    a = [0] * n   

   

    for i in range(n):
        row = input()
        M.append([int(x) for x in row])

    