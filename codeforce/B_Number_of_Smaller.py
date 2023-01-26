n, m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2= list(map(int,input().split()))

pointer1 = 0
res_arr=[]
for element in arr2:
    while pointer1<n and arr1[pointer1] <element:
        pointer1 +=1
    res_arr.append(pointer1)

print(*res_arr)