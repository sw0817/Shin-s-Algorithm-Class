# 백준 12869 뮤탈리스크
# Baekjoon 12869

# Created by sw0817 on 2021. 07. 29..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/12869

from itertools import permutations
from collections import deque

def cal():
    queue = deque()
    queue.append((scv[0], scv[1], scv[2], 0))
    while queue:
        print(queue)
        info = queue.popleft()
        if info[2] == 0:
            return info[3]

        # 두 번째 인자부터는 for문에 접근을 못 하는데 이게 말이 되나
        for attack in attacks:
            next_abc = [0] * 3

            for i in range(3):
                next_abc[i] = info[i] - attack[i] if info[i] - attack[i] > 0 else 0

            next_abc.sort()

            if not visited[next_abc[0]][next_abc[1]][next_abc[2]]:
                visited[next_abc[0]][next_abc[1]][next_abc[2]] = True
                # queue.append((next_abc[0], next_abc[1], next_abc[2], info[3]+1))
                queue.append((*next_abc, info[3] + 1))

N = int(input())
scv = list(map(int, input().split()))
scv.sort(reverse=True)
for _ in range(3-N):
    scv.append(0)

result = 15
visited = [[[False] * 61 for _ in range(61)] for _ in range(61)]
visited[scv[0]][scv[1]][scv[2]] = 1

attacks = permutations([9, 3, 1], 3)

print(cal())