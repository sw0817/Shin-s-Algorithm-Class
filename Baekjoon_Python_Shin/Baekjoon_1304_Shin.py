# 백준 1304 지역
# Baekjoon 1304

# Created by sw0817 on 2021. 12. 21..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1304

def dfs(s, v):
    global top
    if s:
        if grp[v]:
            return
        grp[v] = gtop

    else:
        if visited[v]:
            return
        visited[v] = 1

    for n_v in move[s][v]:
        dfs(s, n_v)

    if not s:
        stk[top] = v
        top += 1



N, M = map(int, input().split())
# move[0][i] : i에서 갈 수 있는 곳
# move[1][i] : i로 갈 수 있는 곳
move = [[[] for _ in range(N+1)] for _ in range(2)]
stk = [0] * N
grp = [0] * (N+1)
top, gtop = 0, 0
visited = [0] * (N+1)

print(move)

for i in range(1, N):
    move[0][i].append(i+1)
    move[1][i+1].append(i)

for _ in range(M):
    s, e = map(int, input().split())
    move[0][s].append(e)
    move[1][e].append(s)

print(move)

for i in range(1, N+1):
    dfs(0, i)

for i in range(top-1, -1, -1):
    if grp[stk[i]]:
        continue
    gtop += 1
    dfs(1, stk[i])

print(grp)
print(stk)
print(gtop)
print(top)