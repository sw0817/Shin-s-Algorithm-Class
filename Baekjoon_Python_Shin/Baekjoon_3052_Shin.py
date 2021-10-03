# 백준 3052 나머지
# Baekjoon 3052

# Created by sw0817 on 2021. 06. 27..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/3052

result_set = set()
for _ in range(10):
    N = int(input())
    result_set.add(N % 42)

print(len(result_set))