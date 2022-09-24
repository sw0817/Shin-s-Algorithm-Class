# 백준 5186 파티를 열어라!!!
# Baekjoon 5186

# Created by sw0817 on 2022. 09. 24..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5186

K = int(input())
for idx in range(K):
    n, c, l = map(int, input().split())
    d = dict()
    for _ in range(n):
        h, i = map(str, input().split())
        h = int(h)
        if h not in d:
            d[h] = [0, 0]
        if i == 'I':
            d[h][0] += 1
        else:
            d[h][1] += 1

    car = []
    for _ in range(c):
        car.append(list(map(int, input().split())))

    car.sort(reverse=True)

    for h, cnt in car:
        if h in d and sum(d[h]) and d[h][1]:
            cur = min(cnt - 1, d[h][0])
            d[h][0] -= cur
            cur2 = min(cnt - cur, d[h][1])
            d[h][1] -= cur2
            n -= cur + cur2

    print("Data Set {}:".format(idx + 1))
    print(n)
