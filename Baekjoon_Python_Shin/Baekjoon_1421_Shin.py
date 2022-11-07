# 백준 1421 나무꾼 이다솜
# Baekjoon 1421

# Created by sw0817 on 2022. 11. 07..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1421

N, C, W = map(int, input().split())
tree = []

for _ in range(N):
    tree.append(int(input()))

result = 0
for i in range(1, max(tree) + 1):
    cur = 0
    for t in tree:
        cur2 = 0
        cnt = t // i
        cur2 += cnt * W * i
        minus = cnt * C

        if not t % i:
            minus -= C

        cur2 -= minus
        if 0 < cur2:
            cur += cur2

    result = max(result, cur)

print(result)