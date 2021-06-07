# 백준 1806 부분합
# Baekjoon 1806

# Created by sw0817 on 2021. 06. 07..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1806

N, S = map(int, input().split())
nums = list(map(int, input().split()))

sum_nums = [0] * (N+1)
for i in range(1, N+1):
    sum_nums[i] = sum_nums[i-1] + nums[i-1]

result = 100001
start = 0
end = 1

while start < N:
    if S <= sum_nums[end] - sum_nums[start]:
        if end - start < result:
            result = end - start
        start += 1

    else:
        if end < N:
            end += 1
        else:
            start += 1

if result < 100001:
    print(result)
else:
    print(0)