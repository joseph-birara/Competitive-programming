n, m, k = map(int, input().split())

player = []
for i in range(m+1):
    player.append(int(input()))
fedor = player[-1]


player.pop()


count = 0
temp = 0
for man in player:

    temp = fedor ^ man

    if bin(temp)[2:].count('1') <= k:
        count += 1
print(count)
