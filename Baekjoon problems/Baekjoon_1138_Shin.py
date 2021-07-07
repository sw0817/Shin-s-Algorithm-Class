# 백준 1138 한 줄로 서기
# Baekjoon 1138

# Created by sw0817 on 2021. 07. 07..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1138

N = int(input())
people = list(map(int, input().split()))
result = [0] * N
for i in range(1, N+1):
    num = people[i-1]
    cnt = 0
    for j in range(N):
        if cnt == num and not result[j]:
            result[j] = i
            break
        elif not result[j]:
            cnt += 1
print(*result)