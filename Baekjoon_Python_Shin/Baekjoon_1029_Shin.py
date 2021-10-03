# 백준 1029 그림 교환
# Baekjoon 1029

# Created by sw0817 on 2021. 08. 09..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1029

# 상태, 번호, 비용, 수
def dfs(num, state, cost, cnt):
    global result
    if cost < dp[num][state]:
        dp[num][state] = cost
        result = max(result, cnt)
    else:
        return

    for i in range(1, N):
        temp = state | (1 << i)
        # i번을 이미 방문했거나, 현재 번호에서 i로 갈때 비용이 더 작거나
        if temp != state and cost <= arr[num][i]:
            # |는 하나라도 켜져 있으면 비트마스킹 켜주기
            dfs(i, temp, arr[num][i], cnt + 1)


N = int(input())

arr = []
for _ in range(N):
    info = input()
    arr += [[]]
    for char in info:
        arr[-1].append(int(char))
# 상태, 번호, 비용
dp = [[10 for _ in range(1 << 15)] for _ in range(N)]
result = 0
dfs(0, 1, 0, 1)
print(result)