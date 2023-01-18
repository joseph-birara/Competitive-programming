n, m = map(int,input().split())
pathBoard = []
for _ in range(n):
    line = input()
    pathBoard.append(line)
for row in range(n):
    if 'S' in pathBoard[row]:
        index = pathBoard[row].indexof('S')
        index2 = index
        while index >0:
            if pathBoard[row][index] =='T':
                print('Yes')
                break
            elif pathBoard[row][index] == '.':
                pathBoard[row][index] 

        for col in range(m):
            if pathBoard[row][col] =='S':
def replaceLetters(vert,hor):
    for 


            





