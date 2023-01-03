n = int(input())
pts = list(map(int,input().split()))
mx, mn = pts[0],pts[0]
res =0
for i in range(1,n):
    if pts[i] > mx or  pts[i] < mn:
        res +=1
    if pts[i] > mx:
        mx =pts[i]
    if pts[i] < mn:
        mn = pts[i]
print(res)

