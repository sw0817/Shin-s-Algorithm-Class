# 백준 15685 드래곤 커브
# Baekjoon 15685

# Created by sw0817 on 2021. 03. 19..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15685

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N = int(input())
arr = [[0] * 101 for _ in range(101)]
result = 0
for _ in range(N):
    y, x, d, n = map(int, input().split())
    arr[x][y] = 1
    queue = [d]
    temp = []
    for _ in range(n+1):
        queue.reverse()
        temp = temp + queue
        for k in queue:
            x += dx[k]
            y += dy[k]
            arr[x][y] = 1
        queue = [(i + 1) % 4 for i in temp]

for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            result += 1

print(result)