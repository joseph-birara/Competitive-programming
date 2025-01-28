# You are given an integer n
# .

# You can perform any of the following operations with this number an arbitrary (possibly, zero) number of times:

# Replace n
#  with n/2
#  if n
#  is divisible by 2
# ;
# Replace n
#  with 2n/3
#  if n
#  is divisible by 3
# ;
# Replace n
#  with 4n/5
#  if n
#  is divisible by 5
# .
# For example, you can replace 30
#  with 15
#  using the first operation, with 20
#  using the second operation or with 24
#  using the third operation.

# Your task is to find the minimum number of moves required to obtain 1
#  from n
#  or say that it is impossible to do it.

# You have to answer q
#  independent queries.

# Input
# The first line of the input contains one integer q
#  (1≤q≤1000
# ) — the number of queries.

# The next q
#  lines contain the queries. For each query you are given the integer number n
#  (1≤n≤1018
# ).

# Output
# Print the answer for each query on a new line. If it is impossible to obtain 1
#  from n
# , print -1. Otherwise, print the minimum number of moves required to do it.

def min_moves(num):
    moves = 0
    while num > 1:
        if num % 2 == 0:
            num = num // 2
        elif num % 3 == 0:
            num = (num * 2) // 3 
        elif num % 5 == 0:
            num = (num * 4) // 5
        else :
            return -1

        moves += 1
    if num == 1:
        return moves
    else :
        return -1
        
q = int (input())

for i in range(q):
    n = int(input())
    print(min_moves(n))