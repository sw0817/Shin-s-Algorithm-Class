# 백준 1446 지름길
# Baekjoon 1446

# Created by sw0817 on 2021. 01. 25..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1446

# 현재위치, 달린거리, 사용 안 한 첫 지름길 idx
def go(l, w, idx):
    global result

    # 사용할 수 있는 모든 지름길에 대해
    for i in range(idx, N):
        start, end, weight = map(int, roads[i])

        # 시작위치 현재위치 이상
        # 도착 위치 목표지점 이하
        # 지름길 타는게 이득인 경우
        # 지름길 탄다.
        if l <= start and end <= D and weight < end - start:
            go(end, w+weight+start-l, i+1)

    # 지름길 안 타고 빨리 갈 수 있으면 그것도 좋아.
    if D - l + w <= result:
        result = D - l + w


N, D = map(int, input().split())

# 정직하게 달리면 10000을 달린다.
result = 10000
roads = [list(map(int, input().split())) for _ in range(N)]

# 앞쪽 지름길부터 확인하기 위해 소팅
roads.sort()

go(0, 0, 0)
print(result)