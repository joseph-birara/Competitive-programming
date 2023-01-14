testCases= int(input())
for _ in range(testCases):
    input()
    board = []
    stoper = True
    for i in range(8):
        temp = input()
        board.append(temp)
   
    for i in range(1,7,1):
        for j in range(1,7,1):
            if board[i][j] == "#":
                if board[i-1][j-1] == "#" and board[i-1][j+1] == "#" and board[i+1][j-1] == "#" and  board[i+1][j+1] == "#":
                    print(i+1,j+1)
                    stoper = False
                    break 
        if stoper == False:
            break

