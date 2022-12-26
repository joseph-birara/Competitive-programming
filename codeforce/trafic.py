t = int(input())
for index in range(t):
    n,c= input().split()
    n= int(n)
    s= input()
    s= s+s
    result =0
    
    for index, letter in enumerate(s):
        if letter == c and c!="g":
            for i in range(index+1,len(s)):
                if s[i] == "g":
                    result =max(result,i-index)
                    break
    print(result)




        