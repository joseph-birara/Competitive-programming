from collections import Counter
t = int(input())

for te in range(t):
   n_fre,n_pre= tuple(map(int,input().split(" ")))
   fre_k = list(map(int,input().split(" ")))
   cost = list(map(int,input().split(" ")))
   
   k_cost = []
   for i,k in enumerate(fre_k):
      k_cost.append([cost[k-1],k])

   k_cost.sort(key = lambda x: -x[0])
   dlr = 0
   j = 1
   for pair in k_cost:
      if  j <= pair[1] and  pair[0] > cost[j-1] :
         d = cost[j-1]
         j +=1
      else: d =  pair[0]
      dlr += d
      
   print(dlr)