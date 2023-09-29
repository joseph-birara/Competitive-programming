def can_vlad_win():
    input()
    num_rooms, num_friends = map(int, input().split())
    friend_rooms = set([room - 1 for room in map(int, input().split())])
    graph = [set() for _ in range(num_rooms)]

    # Build the graph
    for _ in range(num_rooms - 1):
        room_a, room_b = map(int, input().split())
        graph[room_a - 1].add(room_b - 1)
        graph[room_b - 1].add(room_a - 1)

    q_friends = set() | friend_rooms
    q_rooms = set([0])
    visited_rooms = set()

    while True:
        if not q_rooms:
            return "NO"

        next_q_rooms = set()

        for current_room in q_rooms:
            visited_rooms.add(current_room)
            if len(graph[current_room]) == 1 and current_room:
                return "YES"

            for neighbor_room in graph[current_room]:
                if neighbor_room not in visited_rooms and neighbor_room not in friend_rooms:
                    next_q_rooms.add(neighbor_room)

        next_q_friends = set()

        for current_friend in q_friends:
            for neighbor_room in graph[current_friend]:
                if neighbor_room not in friend_rooms:
                    next_q_friends.add(neighbor_room)
                    friend_rooms.add(neighbor_room)

        q_rooms = next_q_rooms - next_q_friends
        q_friends = next_q_friends


num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    result = can_vlad_win()
    print(result)
