n = int(input())
cost =0
quality = -1
min_cost = float('inf')
max_quality = float('-inf')
temp = []


for i in range(n):
    a,b = map(int,input().split())
    temp.append((a,b))
temp.sort()
flag = False
for inde in range(len(temp)-1):


    if temp[inde][1]>temp[inde+1][1]:
        flag = True
        break
if flag == True:
    print("Happy Alex")
else:
    print("Poor Alex")





        


    
    