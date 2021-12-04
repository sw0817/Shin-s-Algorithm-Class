# 백준 21921 블로그
# Baekjoon 21921

# Created by sw0817 on 2021. 12. 04..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/21921

N, X = map(int, input().split())
blog = list(map(int, input().split()))

n = sum(blog[:X])
result = n
x = 1

for i in range(N-X):
    n += blog[i+X] - blog[i]
    if result < n:
        result = n
        x = 1
    elif result == n:
        x += 1

if result:
    print(result)
    print(x)
else:
    print('SAD')