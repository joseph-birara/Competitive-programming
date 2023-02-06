n = int(input())
board =  list(map(int,input().split()))
coin =0
zeros = 0
negative = 0
for i in range(n):
    if board[i] <-1:
        res = -1 - board[i]
        coin += res
        negative +=1
    elif board[i] == 0:
        coin +=1
        zeros +=1
    elif board[i] >1:
        coin += board[i] - 1
    if board[i] == -1:
        negative +=1
if negative %2 !=0:
    if zeros == 0:
        coin += 2
print(coin)
    
    
