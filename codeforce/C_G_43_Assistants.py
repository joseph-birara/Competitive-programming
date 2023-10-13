

t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    students = []
    for _ in range(n):
        s, e = map(int, input().split())
        students.append((s, e))
    end = 0
    for i in range(n):
        end = max(end, students[i][1])
    sol = [0]*(end+1)
    for st in students:
        sol[st[0]] += 1
        sol[st[1]] -= 1
    for i in range(1, end+1):
        sol[i] += sol[i-1]
    print(max(sol))
