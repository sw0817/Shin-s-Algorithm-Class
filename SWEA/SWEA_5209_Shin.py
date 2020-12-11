# SWEA 5209 최소 생산 비용
# SWEA 5209

# Created by sw0817 on 2020. 12. 11..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def find(k, s):
    global result

    if s >= result:
        return

    if k == N:
        if s < result:
            result = s
            return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            find(k+1, s+factory[k][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 100 * N
    find(0, 0)
    print('#{} {}'.format(tc, result))