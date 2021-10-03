# 백준 1986 체스
# Baekjoon 1986

# Created by sw0817 on 2021. 02. 28..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1986

# 나이트와 퀸이 각각 움직일 수 있는 8방 좌표
move_k = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
move_q = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

n, m = map(int, input().split())

# 체스판 상황
array = [[0] * m for _ in range(n)]

# 안전한 위치(sum 함수로 최종 결과값을 구하기 쉽게 우선 모두 안전한 1로 표시)
safe = [[1] * m for _ in range(n)]

# 퀸, 나이트, 폰이 서 있는 위치를 체스판에 표시하고, 안전한 위치에서 삭제한다.
# 퀸과 나이트는 움직일 수 있으므로 따로 그들 위치 배열을 만들어 둠
queens = []
q = list(map(int, input().split()))[1:]
for i in range(len(q) // 2):
    r, c = q[2*i]-1, q[2*i+1]-1
    queens.append((r, c))
    array[r][c] = 1
    safe[r][c] = 0

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

# 모든 퀸에 대해 움직일 수 있는 모든 곳을 안전 배열에서 삭제
# 퀸은 8방으로 중간에 말이 없는 한, 체스판 내에서 무한히 움직일 수 있다.
while queens:
    r, c = queens.pop()
    for dr, dc in move_q:
        nr, nc = r + dr, c + dc
        while 0 <= nr < n and 0 <= nc < m and not array[nr][nc]:
            safe[nr][nc] = 0
            nr += dr
            nc += dc

# 나이트는 현재 위치에서 움직일 수 있는 8자리가 정해져 있다.
while knights:
    r, c = knights.pop()
    for dr, dc in move_k:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            safe[nr][nc] = 0

# 안전 배열의 합을 구하면 답.
result = 0
for i in range(n):
    result += sum(safe[i])

print(result)