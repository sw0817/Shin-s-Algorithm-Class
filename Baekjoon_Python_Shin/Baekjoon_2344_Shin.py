# 백준 2344 거울
# Baekjoon 2344

# Created by sw0817 on 2021. 12. 11..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2344

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# result[i] = 입구 i+1번이 만나는 출구 번호 (서로 대칭)
result = [0] * (2 * N + 2 * M)

# 서로 대칭이므로 왼쪽, 하단 입구만 탐색하여 대칭 작성함
# 시뮬레이션
for i in range(N):
    right = True
    r, c = i, 0
    while 0 <= r < N and 0 <= c < M:
        if arr[r][c]:
            if right:
                right = False
                r -= 1
                continue
            else:
                right = True
                c += 1
                continue
        if right:
            while not arr[r][c]:
                c += 1
                if c == M:
                    break
        else:
            while not arr[r][c]:
                r -= 1
                if r == -1:
                    break
    if c == M:
        result[i] = N + M + (N - r)
        result[N + M + (N - r) - 1] = i + 1
    if r == -1:
        result[i] = 2 * (N + M) - c
        result[2 * (N + M) - c - 1] = i + 1

for j in range(M):
    up = True
    r, c = N-1, j
    while 0 <= r < N and 0 <= c < M:
        if arr[r][c]:
            if up:
                up = False
                c += 1
                continue
            else:
                up = True
                r -= 1
                continue
        if up:
            while not arr[r][c]:
                r -= 1
                if r == -1:
                    break
        else:
            while not arr[r][c]:
                c += 1
                if c == M:
                    break

    if c == M:
        result[N + j] = N + M + (N - r)
        result[N + M + (N - r) - 1] = N + j + 1
    if r == -1:
        result[N + j] = 2 * (N + M) - c
        result[2 * (N + M) - c - 1] = N + j + 1

print(*result)