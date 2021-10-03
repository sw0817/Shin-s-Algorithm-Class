# 백준 1102 발전소
# Baekjoon 1102

# Created by sw0817 on 2021. 08. 11..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1102

def check(state, cost, cnt):
    global result

    if cost < dp[state]:
        dp[state] = cost
    else:
        return

    if P <= cnt:
        result = min(result, cost)
        return

    for j in range(N):
        temp = state | (1 << j)
        if temp != state:
            cur = INF
            for i in range(N):
                if state & (1 << i):
                    cur = min(cur, arr[i][j])
            check(temp, cost + cur, cnt + 1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
onOff = input()
P = int(input())
INF = 16 * 50 + 1
dp = [INF] * (1 << N)
result = INF

state = 0
cnt = 0
for i in range(N):
    if onOff[i] == 'Y':
        state += 2 ** i
        cnt += 1

check(state, 0, cnt)
print(result if not result == INF else -1)