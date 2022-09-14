test = int(input())


for i in range(test):
    n = int(input())
    cont = 0
    ans = False
    if n%2 == 0:
        print(0)
        continue
    elif int(str(n)[0]) % 2 ==0:
        print(1) 
        continue
    else:
        for i in range(1, len(str(n))):
            if int(str(n)[i]) % 2 == 0:
                ans = True
                break
        if ans == True:
            print(2)
        else:
            print(-1)
            
    
 
    
        
