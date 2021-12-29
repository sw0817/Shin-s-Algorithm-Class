# 백준 6593 상범 빌딩
# Baekjoon 6593

# Created by sw0817 on 2021. 12. 29..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/6593

from collections import deque

move = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def bfs():
    t = 0
    queue = deque()
    queue.append(start)
    while queue:
        for _ in range(len(queue)):
            l, r, c = queue.popleft()
            if arr[l][r][c] == 'E':
                print('Escaped in {} minute(s).'.format(t))
                return
            for dl, dr, dc in move:
                nl, nr, nc = l + dl, r + dr, c + dc
                if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and not visited[nl][nr][nc] and not arr[nl][nr][
                                                                                                       nc] == '#':
                    visited[nl][nr][nc] = 1
                    queue.append((nl, nr, nc))
        t += 1
    print('Trapped!')
    return


while True:
    L, R, C = map(int, input().split())
    if not L and not R and not C:
        break
    start = (0, 0, 0)
    end = (0, 0, 0)
    arr = []
    for l in range(L):
        floor = []
        for r in range(R):
            row = list(input())
            floor.append(row)
            for c in range(C):
                if row[c] == 'S':
                    start = (l, r, c)
                elif row[c] == 'E':
                    end = (l, r, c)
        input()
        arr.append(floor)

    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    l, r, c = start
    visited[l][r][c] = 1
    bfs()