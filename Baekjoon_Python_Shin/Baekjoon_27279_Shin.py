# 백준 27279 수 정렬하기
# Baekjoon 27279

# Created by sw0817 on 2023. 01. 31..
# Copyright © 2023 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/27279

def solution():
    N, M = map(int, input().split())
    workCnt = list(map(int, input().split()))
    manCnt = list(map(int, input().split()))
    workCnt.sort(reverse=True)
    manCnt.sort(reverse=True)
    if sum(manCnt) > N:
        return "NO"

    i = 0
    for cnt in manCnt:
        for j in range(i, i + cnt):
            if workCnt[j] < M:
                return "NO"
        M -= 1
        i += cnt

    return "YES"


print(solution())