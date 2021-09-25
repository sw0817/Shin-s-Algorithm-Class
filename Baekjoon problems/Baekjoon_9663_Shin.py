# 백준 9663 N-Queen
# Baekjoon 9663

# Created by sw0817 on 2021. 09. 25..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/9663

def dfs(q_s, n_q):
    global cnt

    if n_q in q_s:
        return

    for r, c in enumerate(q_s):
        h = len(q_s) - r
        if n_q == c + h or n_q == c - h:
            return

    q_s.append(n_q)
    if len(q_s) == N:
        cnt += 1
        return

    for n_q in range(N):
        dfs(q_s[:], n_q)


N = int(input())
cnt = 0
for n_q in range(N):
    q_s = []
    dfs(q_s, n_q)

print(cnt)