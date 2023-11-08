from collections import defaultdict


testCases = int(input())
for _ in range(testCases):
    rows, colums = map(int, input().split())
    board = []
    stoper = True
    for i in range(rows):
        temp = list(map(int, input().split()))
        board.append(temp)

    right = defaultdict(int)
    left = defaultdict(int)
    for row in range(rows):
        for column in range(colums):
            right[row-column] += board[row][column]
            left[row+column] += board[row][column]
    max_sum = 0
    for row in range(rows):
        for column in range(colums):
            max_sum = max(max_sum, (right[row-column]) +
                          (left[row+column]-board[row][column]))
    print(max_sum)
