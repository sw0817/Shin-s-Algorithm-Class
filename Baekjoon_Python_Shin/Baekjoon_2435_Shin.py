# 백준 2435 기상청 인턴 신현수
# Baekjoon 2435

# Created by sw0817 on 2022. 03. 04..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2435

N, K = map(int, input().split())
nums = list(map(int, input().split()))

sums = [0] * (N+1)
sums[1] = nums[0]
for i in range(1, N):
    sums[i+1] = sums[i] + nums[i]

result = -100 * N
for i in range(K, N+1):
    result = max(result, sums[i] - sums[i-K])

print(result)