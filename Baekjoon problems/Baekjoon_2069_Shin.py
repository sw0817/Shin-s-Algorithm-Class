# 백준 2069 보이는 산맥
# Baekjoon 2069

# Created by sw0817 on 2021. 09. 09..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2069

N = int(input())
visited = [False] * N
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))

info = sorted(info, key=lambda x: [x[0], -x[1]])

result = 0
idx = 0
while idx < N:
    if visited[idx]:
        idx += 1
        continue
    visited[idx] = True
    start, end = info[idx]
    if not idx == N-1:
        for j in range(idx + 1, N):
            j_s, j_e = info[j]
            if start <= j_s and j_e <= end:
                visited[j] = True
                continue
            elif end <= j_s:
                result += (end-start) ** 2
                break
            else:
                result += (end - start) ** 2 - (end - j_s) ** 2
                break
        else:
            result += (end - start) ** 2
    else:
        result += (end-start) ** 2

print(result)