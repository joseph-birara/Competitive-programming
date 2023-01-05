grid = [
    [1,2,3,4],
    [6,7,8,9],
    [10,11,12]
]
for k in  zip(*grid):
    print(k)