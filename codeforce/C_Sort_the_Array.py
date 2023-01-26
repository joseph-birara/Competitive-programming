n = int(input())
b = list(map(int,input().split()))
min_index = 0
max_index =0
stor_inde = []

temp = sorted(b)



for i in range(n):
    if b[i] !=temp[i]:
        stor_inde.append(i)
if temp != b:
   
    
    min_index = stor_inde[0]
    max_index = stor_inde[-1]
    reversed_arr = b[min_index:max_index+1]
    sorted_arr = b[0:min_index] + reversed_arr[::-1]+b[max_index+1:]
    if sorted_arr == temp:
        print("yes")
        
        print(min_index+1,max_index+1)
    else:
        print("no")
else:
    print("yes")
    print(1,1)



        
    




