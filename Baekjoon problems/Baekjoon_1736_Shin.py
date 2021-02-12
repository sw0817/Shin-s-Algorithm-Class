# 백준 1736 쓰레기 치우기
# Baekjoon 1736

# Created by sw0817 on 2021. 02. 13..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1736

def find(r):

    # 가장 왼쪽에서 시작
    c = 0
    while r < N:
        temp = c
        arr[r][c] = 0

        # 현재 라인의 쓰레기를 다 치우고, 아랫줄로 내려가 쓰레기 확인
        while c < M and sum(arr[r][c:]):
            arr[r][c] = 0
            c += 1
        if temp != c:
            c -= 1
        r += 1


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

result = 0

for i in range(N):

    # 치울 쓰레기가 있는 라인인 경우
    if sum(arr[i]):

        # 로봇 투입
        result += 1
        find(i)

print(result)
