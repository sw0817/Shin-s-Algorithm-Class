# 백준 14719 빗물
# Baekjoon 14719

# Created by sw0817 on 2021. 06. 21..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/14719

H, W = map(int, input().split())
bricks = list(map(int, input().split()))
max_h = 1
max_idx = 0

for i in range(W):
    if max_h < bricks[i]:
        max_h = bricks[i]
        max_idx = i

sum_ = 0
temp = 0

for i in range(max_idx + 1):
    if temp < bricks[i]:
        temp = bricks[i]
    sum_ += temp

temp = 0
for i in range(W - 1, max_idx, -1):
    if temp < bricks[i]:
        temp = bricks[i]
    sum_ += temp

print(sum_ - sum(bricks))