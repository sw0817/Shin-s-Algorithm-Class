# 백준 5543 상근날드
# Baekjoon 5543

# Created by sw0817 on 2022. 04. 17..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5543

result = -50
cur = 2000
for _ in range(3):
    cur = min(cur, int(input()))
result += cur
cur = 2000
for _ in range(2):
    cur = min(cur, int(input()))
print(result + cur)