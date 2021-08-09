# 백준 1561 놀이 공원
# Baekjoon 1561

# Created by sw0817 on 2021. 08. 09..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1561

N, M = map(int, input().split())
attractions = list(map(int, input().split()))
result = 1

start, end = 0, 30 * 2000000000
if N <= M:
    print(N)
else:
    minute = end
    while start < end:
        mid = (start + end) // 2
        # print(mid)
        # 0초에 M개의 놀이기구에 학생 탑승
        cnt = M
        for i in range(M):
            cnt += mid // attractions[i]
        if N <= cnt:
            end = mid
        else:
            start = mid + 1

    # 현재 cnt = minute에 탑승한 학생 수
    cnt = M
    minute = start
    # print("minute = ", minute)
    for i in range(M):
        cnt += minute // attractions[i]
    # print(cnt)
    for i in range(M-1, -1, -1):
        if not minute % attractions[i]:
            if cnt == N:
                print(i + 1)
                break
            cnt -= 1