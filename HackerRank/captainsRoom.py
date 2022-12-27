# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k = int(input())
numbers = list(map(int,input().split()))
count = Counter(numbers)
for val in count:
    if count[val]<k:
        print(val)
        break
