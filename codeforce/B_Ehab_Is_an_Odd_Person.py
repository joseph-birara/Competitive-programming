def smallest_array(n, a):
    even = False
    odd = False
    for element in a:
        if element %2 ==0:
            even =True
        if element %2 !=0: 
            odd = True
    if odd and even:
        a.sort()
    return a

n = int(input().strip())
a = list(map(int, input().strip().split()))
result = smallest_array(n, a)
print(*result)
