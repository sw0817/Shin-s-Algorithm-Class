# 백준 1450 냅색 문제
# Baekjoon 1450

# Created by sw0817 on 2021. 04. 25..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1450

def left_brute_force(l, w):
    if len(left_weight) <= l:
        left_sum.append(w)
        return

    left_brute_force(l + 1, w)
    left_brute_force(l + 1, w + left_weight[l])


def right_brute_force(l, w):
    if len(right_weight) <= l:
        right_sum.append(w)
        return

    right_brute_force(l + 1, w)
    right_brute_force(l + 1, w + right_weight[l])


def lower_bound(start, end, k):
    global cnt

    while start < end:
        mid = (start + end) // 2

        if right_sum[mid] <= k:
            start = mid + 1
        else:
            end = mid

    return end


N, C = map(int, input().split())
ws = list(map(int, input().split()))
cnt = 0

left_weight = ws[:N//2]
right_weight = ws[N//2:]

left_sum = []
right_sum = []

left_brute_force(0, 0)
right_brute_force(0, 0)
right_sum.sort()

for num in left_sum:
    if C - num < 0:
        continue
    cnt += (lower_bound(0, len(right_sum), C - num))

print(cnt)