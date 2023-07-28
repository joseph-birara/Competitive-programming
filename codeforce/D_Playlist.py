import heapq

num_song, max_select = map(int, input().split())
songs = []

for _ in range(num_song):
    song, beauty = map(int, input().split())
    heapq.heappush(songs, (-beauty, song))

cur_sum = 0
cur_pleasure = 0

while max_select > 0 and songs:
    beauty, song = heapq.heappop(songs)
    beauty = -beauty

    if cur_pleasure > (cur_sum + song) * beauty:
        cur_sum += song
        max_select -= 1
    else:
        cur_pleasure = (cur_sum + song) * beauty
        cur_sum += song
        max_select -= 1

print(cur_pleasure)
