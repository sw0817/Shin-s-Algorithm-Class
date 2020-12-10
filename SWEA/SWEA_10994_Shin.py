# SWEA 10994 동전 수집
# SWEA 10994

# Created by sw0817 on 2020. 12. 10..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXXjAdya60IDFAST&categoryId=AXXjAdya60IDFAST&categoryType=CODE

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    coins = []
    have = [0] * N

    for i in range(N):
        coin, had = map(int, input().split())
        coins.append(coin)
        if had:
            have[i] = 1

    print(coins)
    print(have)

    idx = 0
    while idx < len(coins) and coins[idx] <= K:
        idx += 1

    idx -= 1

    for i in range(idx, -1, -1):
        pass

    # 미완