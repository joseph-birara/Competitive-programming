#accept 3 integers inputs on the same line
import math


n, m, k = map(int, input().split())

lanes =  k/(m*2)

lanes = math.ceil(lanes)

remianing = k - (2*(lanes-1)*m )
desk = math.ceil( remianing/2)

drxn = "R" if k  % 2 == 0  else "L"

print(lanes, desk, drxn)




