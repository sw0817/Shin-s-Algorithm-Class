# 백준 1108 게임
# Baekjoon 1108

# Created by sw0817 on 2021. 03. 27..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1108

def search(r, c):
    global cur
    if not 0 <= r < N or not 0 <= c < M or arr[r][c] == 'H':
        return 0
    if visited[r][c]:
        cur = True
        return -1
    if dp[r][c] != -1:
        return dp[r][c]
    visited[r][c] = 1
    l = arr[r][c]
    for dr, dc in move:
        dp[r][c] = max(dp[r][c], search(r + dr * l, c + dc * l)+1)
        if cur:
            return -1
    visited[r][c] = 0

    return dp[r][c]


move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
arr = []
for _ in range(N):
    row = list(input())
    for i in range(M):
        if row[i].isdigit():
            row[i] = int(row[i])
    arr.append(row)

visited = [[0] * M for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
cur = False

print(search(0, 0))
