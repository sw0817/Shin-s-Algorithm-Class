# 백준 2587 대표값2
# Baekjoon 2587

# Created by sw0817 on 2022. 08. 28..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2587

nums = []
for _ in range(5):
    nums.append(int(input()))

print(sum(nums) // 5)
print(sorted(nums)[2])