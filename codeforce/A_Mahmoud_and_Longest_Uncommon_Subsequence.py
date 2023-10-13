a = input()
b = input()
res = -1

if a == b:
    print(-1)
else:
    if len(a) > len(b):
        print(len(a))
    else:
        print(len(b))
