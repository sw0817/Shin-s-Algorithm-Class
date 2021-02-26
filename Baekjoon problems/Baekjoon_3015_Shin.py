# 백준 3015 오아시스 재결합
# Baekjoon 3015

# Created by sw0817 on 2021. 02. 26..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/3015

N = int(input())

array = []
for i in range(N):
    array.append(int(input()))

result = 0
stack = []
for h in array:
    while stack and stack[-1][0] < h:
        result += stack.pop()[1]

    if not stack:
        stack.append((h, 1))

    else:
        if stack[-1][0] == h:
            cnt = stack.pop()[1]
            result += cnt

            if stack:
                result += 1

            stack.append((h, cnt+1))

        else:
            stack.append((h, 1))
            result += 1

print(result)