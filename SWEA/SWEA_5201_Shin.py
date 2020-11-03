# SWEA 5201 컨테이너 운반
# SWEA 5201

# Created by sw0817 on 2020. 11. 03..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    goods = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    trucks.sort(reverse=True)
    goods.sort(reverse=True)
    result = 0
    visited = [-1] * N
    for i in range(M):
        for j in range(N):
            if trucks[i] >= goods[j] and visited[j] == -1:
                result += goods[j]
                visited[j] = 1
                break

    print('#{} {}'.format(tc, result))