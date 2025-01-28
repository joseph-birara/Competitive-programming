
# C. Coins
# time limit per test2 s.
# memory limit per test512 MB
# In Berland, coins of worth 1
# , 3
#  and 5
#  burles are commonly used (burles are local currency).

# Mihret has to pay exactly n
#  burles in a shop. She has an infinite amount of coins of all three types. However, she doesn't like to pay using coins worth 1
#  burle — she thinks they are the most convenient to use.

# Help Mihret to calculate the minimum number of coins worth 1
#  burle she has to use, if she has to pay exactly n
#  burles. Note that she can spend any number of coins worth 3
#  and/or 5
#  burles.

# Input
# The first line contains one integer t
#  (1≤t≤100
# ) — the number of test cases.

# Each test case consists of one line, containing one integer n
#  (1≤n≤100
# ).

# Output
# For each test case, print one integer — the minimum number of 1
# -burle coins Mihret has to use.


t = int(input())  
for _ in range(t):
    n = int(input())

    
    if n % 3 == 0 or n % 5 == 0:
        print(0)
        continue
    
    remainder = n % 5

    
    if remainder == 1 and n > 5:
        print(0)
    elif remainder == 2 and n > 5:
        print(1)
    elif remainder == 4 and n > 5:
        print(0)
    else:        
        remainder2 = remainder % 3
        print(remainder2)





