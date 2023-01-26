n, m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2= list(map(int,input().split()))

pointer1,pointre2 = 0,0
merged_arr=[]

while pointer1 <n and pointre2<m:
    if arr1[pointer1] < arr2[pointre2]:
        merged_arr.append(arr1[pointer1])
        pointer1+=1
    else:
        merged_arr.append(arr2[pointre2])
        pointre2+=1
    if pointre2==m:
        merged_arr.extend(arr1[pointer1:])
    if pointer1==n:
        merged_arr.extend(arr2[pointre2:])


print(*merged_arr)