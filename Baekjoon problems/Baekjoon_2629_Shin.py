# 백준 2629 양팔저울
# Baekjoon 2629

# Created by sw0817 on 2021. 03. 28..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2629

input()
weights = list(map(int, input().split()))
input()
beads = list(map(int, input().split()))

l = sum(weights) + 1
visited = [0] * l
visited[0] = 1

for weight in weights:
    for i, cur in enumerate(visited[:]):
        if cur:
            if i+weight < l and not visited[i+weight]:
                visited[i+weight] = 1

for weight in weights:
    for i, cur in enumerate(visited[:]):
        if cur:
            if 0 <= i-weight and not visited[i-weight]:
                visited[i-weight] = 1

for bead in beads:
    if len(visited) <= bead:
        print('N', end=' ')
    else:
        if visited[bead]:
            print('Y', end=' ')
        else:
            print('N', end=' ')
