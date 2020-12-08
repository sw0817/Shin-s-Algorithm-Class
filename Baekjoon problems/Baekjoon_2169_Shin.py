# 백준 2169 로봇 조종하기
# Baekjoon 2169

# Created by sw0817 on 2020. 12. 08..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2169

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dist = [[0] * M for _ in range(N)]
left = [[0] * M for _ in range(N)]
right = [[0] * M for _ in range(N)]

dist[0][0] = arr[0][0]
for j in range(1, M):
    dist[0][j] = dist[0][j-1] + arr[0][j]

for i in range(1, N):

    left[i][0] = dist[i-1][0] + arr[i][0]
    for j in range(1, M):
        left[i][j] = arr[i][j] + max(left[i][j-1], dist[i-1][j])

    right[i][-1] = dist[i-1][-1] + arr[i][-1]
    for j in range(M-2, -1, -1):
        right[i][j] = arr[i][j] + max(right[i][j+1], dist[i-1][j])

    for j in range(M):
        dist[i][j] = max(left[i][j], right[i][j])


print(dist[-1][-1])