# 백준 1029 그림 교환
# Baekjoon 1029

# Created by sw0817 on 2021. 08. 08..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1029

def calCnt(lst):
    cnt = 0
    for item in lst:
        if item:
            cnt += 1
    return cnt


def makeState(lst):
    code = 0
    for idx, item in enumerate(lst):
        if item:
            code += 2 ** idx
    return code


def cal(to, flags, cost):
    global result
    cnt = calCnt(flags)
    state = makeState(flags)
    if cost < dp[to][state]:
        dp[to][state] = cost
        result = max(result, cnt)
    else:
        return

    for i in range(N):
        if flags[i] or arr[to][i] < cost:
            continue
        flags[i] = True
        cal(i, flags, arr[to][i])
        flags[i] = False


N = int(input())
arr = []
for i in range(N):
    info = input()
    arr += [[]]
    for char in info:
        arr[-1].append(int(char))

result = 0
dp = [[10 for _ in range(1 << 15 + 1)] for _ in range(N)]
cal(0, [True]+[False]*(N-1), 0)

print(result)