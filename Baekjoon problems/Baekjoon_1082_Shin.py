# 백준 1082 방 번호
# Baekjoon 1082

# Created by sw0817 on 2021. 07. 08..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1082

N = int(input())
cost = list(map(int, input().split()))
money = int(input())

zero = cost[0]

if N == 1:
    print(0)

else:

    min_c = min(cost[1:])
    cnt = 0
    result = ''

    if zero < min_c:
        l = 1 + (money - min_c) // zero
        for i in range(N-1, -1, -1):
            if cnt == 50:
                break
            for j in range(1, 51):
                if 0 <= money - cost[i] and l <= cnt + 1 + (money - cost[i]) // zero:
                    result += str(i)
                    # result = result * 10 + i
                    cnt += 1
                    money -= cost[i]
    else:
        l = money // min_c
        for i in range(N-1, -1, -1):
            if cnt == 50:
                break
            for j in range(1, 51):
                if 0 <= money - cost[i] and l <= cnt + 1 + (money - cost[i]) // min_c:
                    result += str(i)
                    # result = result * 10 + i
                    cnt += 1
                    money -= cost[i]

    print(int(result))
    # print(result)
