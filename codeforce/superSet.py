# Enter your code here. Read input from STDIN. Print output to STDOUT
superSet  = set(list(input().split()))
sub_len= int(input())
res = True

for index in range(sub_len):
    subSet =set(list(input().split()))
    if not superSet.issuperset(subSet):
        res = False
        break
print(res)
    