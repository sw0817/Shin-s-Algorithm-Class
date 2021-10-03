# 백준 2475 검증수
# Baekjoon 2475

# Created by sw0817 on 2021. 06. 27..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2475

nums = list(map(int, input().split()))
result = 0
for num in nums:
    result += num ** 2
print(result % 10)