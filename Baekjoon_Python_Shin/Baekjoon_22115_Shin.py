# 백준 22115 창영이와 커피
# Baekjoon 22115

# Created by sw0817 on 2021. 12. 13..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/22115

import math

N, K = map(int, input().split())
caffeine = [0] + list(map(int, input().split()))
# i 만큼의 카페인 섭취를 위해 마셔야하는 커피 종류 수 배열
dp = [0] + [math.inf] * K
for i in range(1, N+1):
    c = caffeine[i]
    for j in range(K, c-1, -1):
        dp[j] = min(dp[j], dp[j-c]+1)

print(-1 if dp[K] == math.inf else dp[K])