# 백준 10871 X보다 작은 수
# Baekjoon 10871

# Created by sw0817 on 2021. 06. 27..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10871

N, X = map(int, input().split())
nums = list(map(int, input().split()))
result = []
for num in nums:
    if num < X:
        result.append(num)

print(*result)