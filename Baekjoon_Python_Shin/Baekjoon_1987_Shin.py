# 백준 1987 알파벳
# Baekjoon 1987

# Created by sw0817 on 2021. 06. 08..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1987

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(r, c):
    global result
    queue = set()
    queue.add((r, c, board[r][c]))

    while queue:
        r, c, als = queue.pop()

        for dr, dc in move:
            nr, nc = dr + r, dc + c

            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in als:
                queue.add((nr, nc, als + board[nr][nc]))
                result = max(result, len(als)+1)


R, C = map(int, input().split())
board = list(list(input()) for _ in range(R))

result = 1
bfs(0, 0)
print(result)