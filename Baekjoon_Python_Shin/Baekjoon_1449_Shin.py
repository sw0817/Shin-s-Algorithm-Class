# 백준 1449 수리공 항승
# Baekjoon 1449

# Created by sw0817 on 2022. 09. 20..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1449

N, L = map(int, input().split())
locations = list(map(int, input().split()))
locations.sort()
m = 0
L -= 1
cnt = 0
for l in locations:
    if m < l:
        cnt += 1
        m = l + L

print(cnt)