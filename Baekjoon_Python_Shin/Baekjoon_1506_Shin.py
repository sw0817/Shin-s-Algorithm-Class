# 백준 1506 경찰서
# Baekjoon 1506

# Created by sw0817 on 2021. 09. 07..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1506

# scc를 구한다. 타잔 알고리즘을 사용할 것
def dfs(idx):
    global id_num
    d[idx] = id_num
    id_num += 1
    stack.append(idx)

    parent = d[idx]
    for i in range(len(arr[idx])):
        y = arr[idx][i]
        if d[y] == -1:
            parent = min(parent, dfs(y))
        elif not finished[y]:
            parent = min(parent, d[y])

    if parent == d[idx]:
        new_scc = []
        while True:
            t = stack.pop()
            new_scc.append(t)
            finished[t] = True
            if t == idx:
                break

        scc.append(new_scc)

    return parent


N = int(input())
cost = list(map(int, input().split()))
arr = [[] for _ in range(N)]
for i in range(N):
    info = list(map(int, input()))
    for j in range(N):
        if info[j]:
            arr[i].append(j)

d = [-1] * N
scc = []
id_num = 0
stack = []
finished = [False] * (N ** 2)

for i in range(N):
    if d[i] == -1:
        dfs(i)

result = 0

for i in range(len(scc)):
    cur = 1000000
    for n in scc[i]:
        cur = min(cur, cost[n])
    result += cur

print(result)