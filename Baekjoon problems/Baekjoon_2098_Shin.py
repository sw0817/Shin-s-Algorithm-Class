# 백준 2098 욕심쟁이 판다
# Baekjoon 2098

# Created by sw0817 on 2020. 10. 26..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2098


def move(v, w, cnt, sum):
    global result
    if cnt == N:
        if array[v][w] != 0:
            if sum+array[v][w] < result:
                result = sum+array[v][w]
            return

    for j in range(N):
        if array[v][j] != 0 and visited[j] == 0:
            visited[j] = 1
            move(j, w, cnt+1, sum+array[v][j])
            visited[j] = 0


N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
result = 10 ** 10
for i in range(N):
    start = i
    visited = [0] * N
    visited[start] = 1
    move(start, start, 1, 0)

print(result)
