# 백준 1520 내리막 길
# Baekjoon 1520

# Created by sw0817 on 2021. 02. 08..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1520

import sys
sys.setrecursionlimit(100000)

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 거꾸로 올라간다.
def dfs(r, c):
    # 도착지에서 도착지로 가는 방법 수 = 1
    if r == M-1 and c == N-1:
        return 1
    if dp[r][c] != -1:
        # 이미 구한 곳이면 다시 구하지마
        return dp[r][c]
    # 현 위치에서 도착지로 가는 법은 일단은 0개
    dp[r][c] = 0
    for dr, dc in move:
        nr, nc = r + dr, c + dc
        if 0 <= nr < M and 0 <= nc < N and array[nr][nc] < array[r][c]:
            # 현재 위치에서 4방향 중 도착지 가는 방법 수 더하기
            dp[r][c] += dfs(nr, nc)
    # 현재 위치에서 최종 방법 수
    return dp[r][c]


M, N = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]

dfs(0, 0)

# 시작점에서 도착지 가는 방법 수
print(dp[0][0])
