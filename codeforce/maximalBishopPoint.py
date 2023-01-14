from collections import defaultdict


testCases= int(input())
for _ in range(testCases):
    rows,colums = map(int,input().split)
    board = []
    stoper = True
    for i in range(rows):
        temp = list(map(int,input().split()))
        board.append(temp)
   
    # 2 hash maps to hold the sum of diagonal values
    right_hash_map = defaultdict(int)
    left_hash_map = defaultdict(int)
    for row in range(rows):
        for column in range(colums):
            right_hash_map[row-column]+=board[row][column]
           left_hash_map[row+column]+=board[row][column]


