# 백준 1135 뉴스 전하기
# Baekjoon 1135

# Created by sw0817 on 2021. 08. 27..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1135

def solve(i):
    cost = []
    for v in adj[i]:
        cost.append(solve(v))

    if not cost:
        return 0
    cost.sort(reverse=True)
    ret = 0
    for i in range(len(cost)):
        ret = max(ret, cost[i] + i + 1)
    return ret


N = int(input())
adj = [[] for _ in range(N)]
info = list(map(int, input().split()))
for i in range(1, N):
    adj[info[i]].append(i)

print(solve(0))
