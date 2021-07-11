# 백준 2841 외계인의 기타 연주
# Baekjoon 2841

# Created by sw0817 on 2021. 07. 11..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2841

N, P = map(int, input().split())
result = 0
arr = [[] for _ in range(6)]
for _ in range(N):
    n, p = map(int, input().split())
    if len(arr[n-1]):
        while len(arr[n-1]) and p < arr[n-1][-1]:
            result += 1
            arr[n-1].pop()

        if len(arr[n-1]) and arr[n-1][-1] == p:
            continue

        arr[n-1].append(p)
        result += 1

    else:
        result += 1
        arr[n-1].append(p)

print(result)
