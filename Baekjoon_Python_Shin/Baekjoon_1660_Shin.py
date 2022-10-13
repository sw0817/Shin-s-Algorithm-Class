# 백준 1660 캡틴 이다솜
# Baekjoon 1660

# Created by sw0817 on 2022. 10. 13..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1660

import heapq

N = int(input())

nums = []
a, b, i = 0, 0, 1

while b <= N:
    a += i
    i += 1
    b += a
    nums.append(b)

nums.pop(-1)
nums.sort(reverse=True)
dp = [300000] * (N + 1)
queue = []
for n in nums:
    heapq.heappush(queue, -n)
    dp[n] = 1

while queue:
    cur = -heapq.heappop(queue)
    cnt = dp[cur]
    for n in nums:
        n_cur = cur + n
        if n_cur <= N and cnt + 1 < dp[n_cur]:
            heapq.heappush(queue, -n_cur)
            dp[n_cur] = cnt + 1

print(dp[N])