# 백준 1365 꼬인 전깃줄
# Baekjoon 1365

# Created by sw0817 on 2021. 06. 15..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1365

# 해당 숫자 이상의 수 중 가장 가까운 index를 return (정렬 시)
def lower_bound(s, e, v):
    while s < e:
        m = (s + e) // 2
        if res[m] < v:
            s = m + 1
        else:
            e = m
    return e


N = int(input())
rights = list(map(int, input().split()))
res = []

res.append(rights[0])

for i in range(1, N):
    if res[-1] < rights[i]:
        res.append(rights[i])
    else:
        temp = lower_bound(0, len(res), rights[i])
        res[temp] = rights[i]

print(N-len(res))
