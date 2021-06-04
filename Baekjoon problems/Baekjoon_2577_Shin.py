# 백준 2577 숫자의 개수
# Baekjoon 2577

# Created by sw0817 on 2021. 06. 04..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2577

nums = [str(i) for i in range(10)]
A = int(input())
B = int(input())
C = int(input())
numStr = str(A * B * C)
l = len(numStr)
result = [0] * 10
for i in range(l):
    result[nums.index(numStr[i])] += 1

for i in range(10):
    print(result[i])
