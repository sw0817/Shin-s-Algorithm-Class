# 백준 1937 욕심쟁이 판다
# Baekjoon 1937

# Created by sw0817 on 2021. 02. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1937

import sys

sys.setrecursionlimit(100000)
next = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def feed(i, j):
    # 방문 안 했으면
    if not dp[i][j]:
        for dr, dc in next:
            nr = i + dr
            nc = j + dc
            if 0 <= nr < N and 0 <= nc < N and arr[i][j] < arr[nr][nc]:
                # nr, nc 에서 조건 맞는 경우 그곳을 시작점으로 하는 return 값과 비교
                # 갈 곳이 있다면 재귀를 들어가므로 가장 깊숙히 들어간 곳(움직일 곳이 없는)부터
                # 아래 하루를 산다를 행한다.
                dp[i][j] = max(dp[i][j], feed(nr, nc))

        # 하루를 산다.
        dp[i][j] += 1

    # 산 기간 return
    return dp[i][j]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 방문 배열이자 각 위치 시작으로 며칠 살 수 있는지 나타내는 dp배열
dp = [[0] * N for _ in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        # 모든 위치에서 최대값 갱신
        result = max(result, feed(i, j))

print(result)