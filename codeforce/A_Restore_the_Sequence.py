testCases = int(input())
for _ in range(testCases):
    n = int(input())
    boadrS =  list(map(int,input().split()))
    left = 0
    right = n-1
    temp =[]
    while left < right:
        temp.append(boadrS[left])
        temp.append(boadrS[right])
        left +=1
        right -=1
    if len(temp)<n:
        temp.append(boadrS[right])
    print(*temp)


