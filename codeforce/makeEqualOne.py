n = int(input())
a = list(map(int, input().split()))

positive = 0
negative = 0
zero = 0

step = 0

for i in range(n):
    
    
    if (a[i] == 0):
        zero += 1
        
   
    elif (a[i] < 0):

        negative += 1
        step = step + (-1 - a[i])

    else:
        positive += 1
        step = step + (a[i] - 1)
if (negative % 2 == 0):
    step = step + zero

else:
    if (zero > 0):
        step = step + zero
    else:
        step = step + 2
print(step) 

