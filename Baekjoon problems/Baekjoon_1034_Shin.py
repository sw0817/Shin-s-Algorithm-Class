# 백준 1034 램프
# Baekjoon 1034

# Created by sw0817 on 2021. 04. 21..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1034

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
K = int(input())
cnt = [0] * N
if K % 2:
    for i in range(N):
        zero = arr[i].count('0')
        if zero % 2 and zero <= K:
            for j in range(N):
                if arr[i] == arr[j]:
                    cnt[i] += 1
else:
    for i in range(N):
        zero = arr[i].count('0')
        if not zero % 2 and zero <= K:
            for j in range(N):
                if arr[i] == arr[j]:
                    cnt[i] += 1

print(max(cnt))