# 백준 1326 폴짝폴짝
# Baekjoon 1326

# Created by sw0817 on 2021. 12. 03..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1326

from collections import deque

def bfs():
    queue = deque()
    queue.append(a)
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            i = queue.popleft()
            i2 = i

            if i == b:
                return cnt

            x = bridge[i]
            while i + x < N + 1:
                i += x
                if not visited[i]:
                    visited[i] = 1
                    queue.append(i)

            while 0 < i2 - x:
                i2 -= x
                if not visited[i2]:
                    visited[i2] = 1
                    queue.append(i2)
        cnt += 1
    return -1


N = int(input())
bridge = [0] + list(map(int, input().split()))
a, b = map(int, input().split())
visited = [0] * (N+1)
visited[a] = 1
print(bfs())