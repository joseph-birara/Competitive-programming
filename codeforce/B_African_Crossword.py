from collections import Counter


n,m = map(int,input().split())
board = []

resultdStr= ''

for _ in range(n):
    board.append(input())
for index in range(n):
    for innerIndex in range(m):
        temp = ''
        if board[index][innerIndex] not in temp:
            reapeted = False
            for row in range(n):
                if row !=index:
                    if board[row][innerIndex] ==board[index][innerIndex]:
                        reapeted = True
                        temp +=board[index][innerIndex]
                        break
            for col in range(m):
                if col !=innerIndex:
                    if board[index][col] ==board[index][innerIndex]:
                        reapeted = True
                        temp +=board[index][innerIndex]
                        break
            if reapeted ==False:
                resultdStr+=board[index][innerIndex]
print(resultdStr)
                    


        


