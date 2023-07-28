number = int(input())

mati = list(map(int, input().split()))
ibsa = list(map(int, input().split()))
mati.sort()
ibsa.sort()

pt1 = pt2 = 0
ibsa_score = 0

while pt1 < number and pt2 < number:
    while pt2 < number and ibsa[pt2] < mati[pt1]:
        pt2 += 1
    if pt2 < number:
        ibsa_score += 1
    pt1 += 1
    pt2 += 1
if ibsa_score > number//2:
    print("YES")
else:
    print("NO")
