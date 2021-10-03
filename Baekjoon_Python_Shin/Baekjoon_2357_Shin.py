# 백준 2357 최솟값과 최댓값
# Baekjoon 2357

# Created by sw0817 on 2021. 09. 05..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2357

import math
from sys import stdin

# 세그먼트 트리를 구현한다.
def initMin(node, start, end):
    if start == end:
        tree_min[node] = arr[start]
        return tree_min[node]

    mid = (start + end) // 2
    tree_min[node] = min(initMin(node * 2, start, mid), initMin(node * 2 + 1, mid + 1, end))
    return tree_min[node]


def initMax(node, start, end):
    if start == end:
        tree_max[node] = arr[start]
        return tree_max[node]

    mid = (start + end) // 2
    tree_max[node] = max(initMax(node * 2, start, mid), initMax(node * 2 + 1, mid+1, end))
    return tree_max[node]


def queryMin(node, start, end, left, right):
    if start > right or end < left:
        return 1000000001

    if left <= start and end <= right:
        return tree_min[node]

    mid = (start + end) // 2
    return min(queryMin(node * 2, start, mid, left, right), queryMin(node * 2 + 1, mid + 1, end, left, right))


def queryMax(node, start, end, left, right):
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return tree_max[node]

    mid = (start + end) // 2
    return max(queryMax(node * 2, start, mid, left, right), queryMax(node * 2 + 1, mid + 1, end, left, right))


N, M = map(int, stdin.readline().split())

# 세그먼트 트리 높이 계산
h = int(math.ceil(math.log2(N)))
# 대략적 트리 노드 개수
t_size = 1 << (h+1)

arr = []
tree_min = [0] * t_size
tree_max = [0] * t_size

for _ in range(N):
    arr.append(int(stdin.readline()))

initMax(1, 0, N-1)
initMin(1, 0, N-1)

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    print(queryMin(1, 0, N-1, a-1, b-1), end=" ")
    print(queryMax(1, 0, N-1, a-1, b-1))