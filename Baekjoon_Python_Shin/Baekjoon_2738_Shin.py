# 백준 2738 행렬 덧셈
# Baekjoon 2738

# Created by sw0817 on 2022. 08. 18..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2738

N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
mat2 = [list(map(int, input().split())) for _ in range(N)]
ret = [list(mat[i][j] + mat2[i][j] for j in range(M)) for i in range(N)]

for row in ret:
    print(*row)