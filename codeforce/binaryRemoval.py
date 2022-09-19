n = int(input())
for _ in range(n):
    s = input()
    zero = 0
    one = len(s)
    for i in range(len(s)-1):
        if s[i]==s[i+1] and s[i]=="1":
            one = i+1
            break
    for i in range(1,len(s)):
        if s[-i]==s[-(i+1)] and s[-i]=="0":
            zero = len(s)-i
            break
    if zero>one:
        print("No")
    else:
        print("Yes")