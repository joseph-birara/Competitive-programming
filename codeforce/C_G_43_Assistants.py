def max_overlapping_intervals(test_cases):
    for case in test_cases:
        n = case[0]
        students = case[1:]
        events = []

        for i in range(n):
            start_time, end_time = students[i]
            events.append((start_time, 1))
            events.append((end_time, -1))

        events.sort()

        max_overlaps = 0
        current_overlaps = 0

        for _, event_type in events:
            if event_type == 1:
                current_overlaps += 1
            else:
                current_overlaps -= 1

            max_overlaps = max(max_overlaps, current_overlaps)

        print(max_overlaps)


t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    students = []
    for _ in range(n):
        s, e = map(int, input().split())
        students.append((s, e))
    test_cases.append([n] + students)

max_overlapping_intervals(test_cases)
