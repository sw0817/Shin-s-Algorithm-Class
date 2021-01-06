# 백준 2562 최댓값
# Baekjoon 2562

# Created by sw0817 on 2020. 01. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2562

result = 0
idx = 0
for i in range(9):
    number = int(input())
    if result < number:
        result = number
        idx = i+1

print(result)
print(idx)