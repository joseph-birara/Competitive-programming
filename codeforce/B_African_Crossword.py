from collections import Counter


n,m = map(int,input().split())
board = []
resultdStr= ''

for _ in range(n):
    board.append(input())
for index in range(n):
    for innerIndex in range(m):
        print(board[index])
        countInRow = Counter(board[index])
        print(zip(*board))
        countInCol =Counter(zip(*board[index]))


