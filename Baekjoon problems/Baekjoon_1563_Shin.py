# 백준 1563 개근상
# Baekjoon 1563

# Created by sw0817 on 2021. 07. 27..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1563

from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

def cal(day, late, absent):
    if 2 <= late or 3 <= absent:
        return 0
    if day == N:
        return 1
    if dp[day][late][absent] != 0:
        return dp[day][late][absent]

    # 다음 출석
    dp[day][late][absent] += cal(day+1, late, 0)
    # 다음 지각
    dp[day][late][absent] += cal(day+1, late+1, 0)
    # 다음 결석
    dp[day][late][absent] += cal(day+1, late, absent+1)

    return dp[day][late][absent] % 1000000


N = int(input())

dp = [[[0] * 3 for _ in range(2)] for _ in range(N)]

print(cal(0, 0, 0) % 1000000)