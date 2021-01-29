# 백준 4191 Dominos 2
# Baekjoon 4191

# Created by sw0817 on 2021. 01. 29..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/4191

# 영어 문제 첫 도전입니다.
from _collections import deque


T = int(input())

for tc in range(T):

    # n, m, l <= 10000
    # n = 노미노 타일 수 (1 ~ n번 넘버링)
    n, m, l = map(int, input().split())

    # 넘어짐 여부, 다음 넘어질 도미노 배열
    dominos = [0] * n
    nexts = [[] for _ in range(n)]

    for _ in range(m):

        # x가 넘어지면 y가 넘어진다.
        x, y = map(int, input().split())
        nexts[x-1].append(y-1)

    for _ in range(l):

        # z를 손으로 넘어뜨린다.
        z = int(input())

        # 아직 넘어지지 않은 도미노면 큐에 넣는다.
        if not dominos[z-1]:
            queue = deque()
            queue.append(z-1)

            while queue:
                d = queue.pop()

                # 마찬가지로, 큐에서 pop한 도미노가 넘어졌으면 continue
                if dominos[d]:
                    continue

                # 아니라면 넘어뜨리고,
                dominos[d] = 1

                # 다음 도미노들의 넘어짐 여부를 판단.
                for nd in nexts[d]:
                    if dominos[nd]:
                        continue

                    # 안 넘어졌으면 큐에 추가
                    queue.append(nd)

    # 넘어진 수를 더한다.
    print(sum(dominos))