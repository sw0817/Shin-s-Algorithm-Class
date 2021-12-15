# 백준 1037 약수
# Baekjoon 1037

# Created by sw0817 on 2021. 12. 15..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1037

n = int(input())
nums = list(map(int, input().split()))
print(min(nums) * max(nums))