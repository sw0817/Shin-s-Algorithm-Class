# 백준 1978 소수 찾기
# Baekjoon 1978

# Created by sw0817 on 2022. 11. 08..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1978

N = int(input())
nums = map(int, input().split())
cnt = 0
for i in nums:
    flag = 0
    if 1 < i:
        for j in range(2, i // 2 + 1):
            if not i % j:
                break
        else:
            cnt += 1

print(cnt)