# 백준 1419 등차수열의 합
# Baekjoon 1419

# Created by sw0817 on 2021. 07. 19..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1419

# 실패

left = int(input())
right = int(input())
k = int(input())

cur = int(k * (k+1) / 2)

if right < cur:
    print(0)
else:
    a = right - cur
    b = left - cur
    c = a // k + 1
    # print(a, b, c)
    # if a % k:
    #     c += 1
    d = b // k + 1
    if not b % k and 0 < d:
        d -= 1
    if left <= cur:
        print(c)
    else:
        print(c - d)



# if left <= cur:
#     a = right // k - cur // k
#     if not cur % k:
#         a += 1
# else:
#     a = right // k - left // k
#     if not left % k:
#         a += 1

# print(a)