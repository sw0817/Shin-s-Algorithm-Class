# 백준 2024 선분 덮기
# Baekjoon 2024

# Created by sw0817 on 2022. 02. 26..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2024

M = int(input())
lines = []
line_dict = dict()
while True:
    l, r = map(int, input().split())
    if r < 0 or M < l:
        continue
    if not l and not r:
        break
    if not l in line_dict:
        line_dict[l] = r
    else:
        line_dict[l] = max(line_dict[l], r)

for l in line_dict:
    lines.append((l, line_dict[l]))

lines.sort()

result = 0

cur_l = 0
cur_r = 0

cnt = len(lines)
idx = 0
max_r = 0
while idx < cnt:
    while idx < cnt and lines[idx][0] <= cur_r:
        max_r = max(max_r, lines[idx][1])
        idx += 1
    if cur_r < max_r:
        cur_r = max_r
        result += 1
    else:
        result = 0
        break
    if M <= max_r:
        break

print(result)