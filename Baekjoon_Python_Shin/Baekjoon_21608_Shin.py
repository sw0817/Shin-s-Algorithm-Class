# 백준 21608
# Baekjoon 21608

# Created by sw0817 on 2021. 11. 20..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/21608

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N = int(input())
arr = [[0] * N for _ in range(N)]
final = [0] * (N**2)
for _ in range(N ** 2):
    info = list(map(int, input().split()))
    n = info[0]
    likes = info[1:]
    final[n-1] = likes[:]
    empty = 0
    like_cnt = 0
    locate = [N, N]
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if arr[i][j]:
                continue
            cur_empty = 0
            cur_like = 0
            for dr, dc in delta:
                r, c = i + dr, j + dc
                if 0 <= r < N and 0 <= c < N:
                    if arr[r][c] == 0:
                        cur_empty += 1
                    elif arr[r][c] in likes:
                        cur_like += 1
            if like_cnt < cur_like:
                like_cnt = cur_like
                locate = [i, j]
                empty = cur_empty
            elif like_cnt == cur_like and empty <= cur_empty:
                empty = cur_empty
                locate = [i, j]
    r, c = locate
    arr[r][c] = n

result = 0
for i in range(N):
    for j in range(N):
        n = arr[i][j]
        cnt = 0
        for dr, dc in delta:
            r, c = i + dr, j + dc
            if 0 <= r < N and 0 <= c < N:
                if arr[r][c] in final[n-1]:
                    cnt += 1
        if cnt:
            result += 10 ** (cnt-1)

print(result)