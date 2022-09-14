n = int(input())
a ,b = map(int,input().split())
c ,d = map(int,input().split())
e ,f = map(int,input().split())
 
	
	
	
if(c<a and e<a and d<b and f<b):
 
    if(e-a!=f-b):
        print("YES")
    else:
        print("NO")
 
elif(c<a and e<a and d>b and f>b):
    
 
    if(e-a!=f-b):
    
        print("YES")
    else:
        print("NO")
 
elif(c>a and e>a and d<b and f<b):
 
    if(e-a!=f-b):
        print("YES")
    else:
        print("NO")
 
elif(c>a and e>a and d>b and f>b):
    
 
    if(e-a!=f-b):
        
        print("YES")
    else:
        print("NO")
 
else:
    
    print("NO")