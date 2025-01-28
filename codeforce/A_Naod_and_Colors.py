
#accept interger input
    



num = int(input())

for i in range(num):
    #accept integer input
    n = int(input())
    #accept n integers in to a list
    a = list(map(int, input().split()))
    #print the most frequent elememnt
    print(a.count(max(set(a), key = a.count)))  


    
   
