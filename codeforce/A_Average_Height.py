 
testcase = int(input())
 
for i in range(testcase):
    people = int(input())
    height = list(map(int , input().split()))
 
    odd = []
    even = []
 
    for h in height:
        if h% 2== 0:
            even.append(h)
        else:
            odd.append(h)
    print(*(odd + even))