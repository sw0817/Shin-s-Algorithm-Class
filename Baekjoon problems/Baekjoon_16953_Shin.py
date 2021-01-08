# 백준 16953 A -> B
# Baekjoon 16953

# Created by sw0817 on 2021. 01. 08..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/16953

def cal(cnt, n):
    global result
    if result <= cnt or B < n:
        return
    if n == B:
        result = cnt
        return
    cal(cnt+1, n*10+1)
    cal(cnt+1, n*2)


A, B = map(int, input().split())
result = 999999999
cal(1, A)
if result == 999999999:
    print(-1)
else:
    print(result)