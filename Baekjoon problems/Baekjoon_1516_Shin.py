# 백준 1516 게임 개발
# Baekjoon 1516

# Created by sw0817 on 2020. 12. 20..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1516

N = int(input())

build = []
done = [0] * N

for i in range(N):
    build.append(list(map(int, input().split())))

T = 0
B = 0

while B != N:
    queue = []
    min_time = 1000001
    for i in range(N):
        if not done[i]:
            check = 1
            for j in range(1, len(build[i])-1):
                if not done[build[i][j]-1]:
                    check = 0
                    break
            if check:
                queue.append(i)
                if build[i][0] < min_time:
                    min_time = build[i][0]
    T += min_time
    for i in range(len(queue)):
        build[queue[i]][0] -= min_time
        if build[queue[i]][0] == 0:
            done[queue[i]] = T
            B += 1

for i in range(N):
    print(done[i])