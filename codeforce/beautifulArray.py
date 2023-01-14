length = int(input())
arr = list(map(int,input().split()))
setOne = []
setTwo = []
setThree = []
extra = []

for element in arr:
    if element == 0:
        setThree.append(element)   
    elif  len(setOne) ==0 and element < 0:
        setOne.append(element)
    elif element > 0:
         setTwo.append(element) 
    else:
        extra.append(element)  
if len(setTwo) == 0:
    setTwo.append(extra.pop())
    setTwo.append(extra.pop())
setThree.extend(extra)


              


print(len(setOne),*setOne)
print(len(setTwo),*setTwo)
print(len(setThree),*setThree)
