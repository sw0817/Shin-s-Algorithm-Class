# 백준 1636 한번 열면 멈출 수 없어
# Baekjoon 1636

# Created by sw0817 on 2022. 03. 28..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1636

N = int(input())
result = 0
min_, max_ = map(int, input().split())
cur = 0
age = [0] * N
for i in range(N-1):
    l, r = map(int, input().split())
    if l <= cur <= r:
        if cur:
            age[i+1] = cur
        continue

    if cur:
        if l <= min_ <= r or min_ <= l <= max_:
            continue
        if cur < l:
            result += l - cur
            cur = l
            age[i+1] = cur
        else:
            result += cur - r
            cur = r
            age[i+1] = cur
    else:
        if l <= min_ <= r or min_ <= l <= max_:
            min_ = max(min_, l)
            max_ = min(max_, r)
        else:
            idx = i
            if max_ < l:
                while 0 <= idx and not age[idx]:
                    age[idx] = max_
                    idx -= 1
                result += l - max_
                cur = l
                age[i+1] = cur
            elif r < min_:
                while 0 <= idx and not age[idx]:
                    age[idx] = min_
                    idx -= 1
                result += min_ - r
                cur = r
                age[i+1] = cur

if not cur:
    for i in range(N):
        age[i] = min_

print(result)

for i in range(N):
    print(age[i])