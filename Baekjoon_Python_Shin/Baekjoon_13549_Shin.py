# 백준 13549 숨바꼭질 3
# Baekjoon 13549

# Created by sw0817 on 2021. 01. 11..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/13549

def next():
    queue = [N]
    while queue:
        l = queue.pop(0)
        if l == K:
            return visited[l]
        for nl in (l-1, l+1, 2*l):
            if 0 <= nl <= 100000 and not visited[nl]:
                if l != 0 and nl == 2*l:
                    visited[nl] = visited[l]
                    queue.insert(0, nl)
                else:
                    visited[nl] = visited[l] + 1
                    queue.append(nl)


N, K = map(int, input().split())

visited = [0] * 100001
result = 100000

print(next())
