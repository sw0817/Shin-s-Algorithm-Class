# 백준 2212 센서
# Baekjoon 2212

# Created by sw0817 on 2021. 02. 24..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2212

N = int(input())
K = int(input())

# 겹치는 좌표의 센서 제거
sensors = list(set(list(map(int, input().split()))))

# 위치 순으로 정렬
sensors.sort()

# 센서끼리의 거리 차이 배열
Ls = []
for i in range(1, len(sensors)):
    Ls.append(sensors[i]-sensors[i-1])

# 배열을 거리 길이 순으로 정렬
Ls.sort()

# 모든 센서에 집중국을 설치할 수 있으면 수신거리는 0
if len(Ls) < K:
    print(0)

else:
    # K-1 개의 가장 긴 센서 사이 거리를 무시할 수 있다.
    print(sum(Ls[:len(Ls)-K+1]))