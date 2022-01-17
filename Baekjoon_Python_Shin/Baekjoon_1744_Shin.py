# 백준 1744 수 묶기
# Baekjoon 1744

# Created by sw0817 on 2022. 01. 17..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1744

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

numbers.sort()
result = 0
l = 0
r = len(numbers)
while l < r and numbers[l] < 0:
    if l == r - 1:
        result += numbers[l]
        l += 1
        continue
    if numbers[l+1] <= 0:
        result += numbers[l] * numbers[l+1]
        l += 2
    else:
        result += numbers[l]
        l += 1

r -= 1
while l <= r and 0 < numbers[r]:
    if l < r and 1 < numbers[r-1]:
        result += numbers[r] * numbers[r-1]
        r -= 2
    else:
        result += numbers[r]
        r -= 1

print(result)