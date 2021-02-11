# 백준 1069 집으로
# Baekjoon 1069

# Created by sw0817 on 2021. 02. 12..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1069

import math


X, Y, D, T = map(int, input().split())

# (X, Y) 에서 (0, 0) 까지 직선거리
length = math.sqrt((X ** 2 + Y ** 2))

# (0, 0)을 넘지 않으면서 직선 방향으로 점프할 수 있는 최대 횟수
initial = length // D

# 그때 남은 거리
left = length - initial * D

# 한 번도 뛸 수 없다면,
if initial == 0:

    # 그냥 걸어가거나, 넘어가게 뛴 후 남은 거리 걷기, 두 번 점프로 도착하기 중 최소시간
    result = min(length, T + D - left, 2 * T)

# 여러 번 뛰는게 가능하다면
else:

    # 그냥 걸어가거나, 최대한 뛴 다음 걸어가거나, 최대한 뛰다가 마지막에 두 번 점프로 도착하기 중 최소시간
    result = min(length, initial * T + left, T * (initial + 1))

print(result)

