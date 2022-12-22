# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
temp = {}
res =0
for i in range(n):
    word = input()
    if word not in temp.keys():
        res+=1
        temp[word]=1
    else:
         temp[word]+=1
print(res)
val=' '.join(str(x) for x in temp.values())
print(val)