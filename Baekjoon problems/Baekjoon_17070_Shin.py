# 백준 17070 최소 힙
# Baekjoon 17070

# Created by sw0817 on 2020. 10. 15..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/17070


N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0] * 3 for _ in range(N)] for _ in range(N)]
first_state = 1
visited[0][1][0] = 1
for c in range(2, N):
    if house[0][c] == 0:
        visited[0][c][0] = visited[0][c-1][0]

for r in range(N):
    for c in range(2, N):
        if house[r][c] == house[r][c-1] == house[r-1][c] == 0:
            visited[r][c][2] = visited[r-1][c-1][0] + visited[r-1][c-1][1] + visited[r-1][c-1][2]
        if house[r][c] == 0:
            visited[r][c][0] = visited[r][c-1][2] + visited[r][c-1][0]
            visited[r][c][1] = visited[r-1][c][2] + visited[r-1][c][1]


print(sum(visited[-1][-1]))