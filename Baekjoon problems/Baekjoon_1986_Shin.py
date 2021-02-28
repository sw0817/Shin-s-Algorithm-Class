# 백준 1986 체스
# Baekjoon 1986

# Created by sw0817 on 2021. 02. 28..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1986

move_k = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
move_q = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


n, m = map(int, input().split())

array = [[0] * m for _ in range(n)]
safe = [[1] * m for _ in range(n)]

queens = []
q = list(map(int, input().split()))[1:]
for i in range(len(q) // 2):
    r, c = q[2*i]-1, q[2*i+1]-1
    queens.append((r, c))
    array[r][c] = 1

knights = []
k = list(map(int, input().split()))[1:]
for i in range(len(k) // 2):
    r, c = k[2*i]-1, k[2*i+1]-1
    knights.append((r, c))
    array[r][c] = 1
    safe[r][c] = 0

p = list(map(int, input().split()))[1:]
for i in range(len(p) // 2):
    r, c = p[2*i]-1, p[2*i+1]-1
    array[r][c] = 1
    safe[r][c] = 0

while queens:
    r, c = queens.pop()
    safe[r][c] = 0
    for dr, dc in move_q:
        nr, nc = r + dr, c + dc
        while 0 <= nr < n and 0 <= nc < m and not array[nr][nc]:
            safe[nr][nc] = 0
            nr += dr
            nc += dc

while knights:
    r, c = knights.pop()
    for dr, dc in move_k:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            safe[nr][nc] = 0

result = 0
for i in range(n):
    result += sum(safe[i])

print(result)