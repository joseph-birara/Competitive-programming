n = int(input())
artifacts = list(map(int, input().split()))
total_energy = sum(artifacts)
can_reach = [False] * (total_energy + 1)
can_reach[0] = True
for artifact_energy in artifacts:
    for i in range(total_energy, -1, -1):
        if can_reach[i]:
            can_reach[i + artifact_energy] = True
for i in range(1, total_energy + 1):
    if not can_reach[i]:
        print(i)
        break
