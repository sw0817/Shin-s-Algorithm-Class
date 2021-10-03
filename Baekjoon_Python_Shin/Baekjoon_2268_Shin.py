# 백준 2268 수들의 합
# Baekjoon 2268

# Created by sw0817 on 2021. 09. 06..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2268

import math
from sys import stdin

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]


def update(node, start, end, idx, diff):
    if start > idx or end < idx:
        return

    tree[node] += diff

    if not start == end:
        mid = (start + end) // 2
        update(node * 2, start, mid, idx, diff)
        update(node * 2 + 1, mid + 1, end, idx, diff)


def query(node, start, end, i, j):
    if end < i or j < start:
        return 0

    if i <= start and end <= j:
        return tree[node]

    mid = (start + end) // 2
    return query(node * 2, start, mid, i, j) + query(node * 2 + 1, mid + 1, end, i, j)


N, M = map(int, stdin.readline().split())
# 세그먼트 트리 높이 계산
h = int(math.ceil(math.log2(N)))
# 대략적 트리 노드 개수
t_size = 1 << (h+1)
tree = [0] * t_size
arr = [0] * (N+1)
init(1, 1, N)

for _ in range(M):
    s, i, j = map(int, stdin.readline().split())
    if s:
        diff = j - arr[i]
        arr[i] = j
        update(1, 1, N, i, diff)
    else:
        if i > j:
            i, j = j, i
        print(query(1, 1, N, i, j))