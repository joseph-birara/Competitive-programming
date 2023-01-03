n = int(input())
result =[]
for i in range(n):
    result.append(input())
d = len(result[0])

pt =''  
for k in range(d):
    set_temp = set()
    for m in range(n):
        set_temp.add(result[m][k])
    if len(set_temp) >2:
        pt+='?'
    elif len(set_temp) == 1:
        for x in set_temp:
            if x == "?":
                pt+="x"
            else:
                pt+=x
    else:
        flag =0
        le =''
        for y in set_temp:
            if y != "?":
                flag +=1
                le = y
        if flag ==1:
            pt+=le
        if flag ==2:
            pt+="?"
print(pt)
            


        
        
    


    
