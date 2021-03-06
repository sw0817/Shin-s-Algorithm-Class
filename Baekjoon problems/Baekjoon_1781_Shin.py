# 백준 1781 컵라면
# Baekjoon 1781

# Created by sw0817 on 2021. 03. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1781

N = int(input())
ramen = []
for _ in range(N):
    ramen.append(list(map(int, input().split())))

ramen.sort()
cups = []

for info in ramen:
    deadline = info[0]
    cups.append(info[1])
    while deadline < len(cups):
        cups.remove(min(cups))

print(sum(cups))