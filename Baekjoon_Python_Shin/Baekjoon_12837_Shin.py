# 백준 12837 가계부 (Hard)
# Baekjoon 12837

# Created by sw0817 on 2021. 04. 02..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/12837

import sys, math

def initSegmentTree(arr, segmentTree, node, left, right):
    if left == right:
        segmentTree[node] = arr[left]
    else:
        mid = (left + right) // 2
        segmentTree[node] = (initSegmentTree(arr, segmentTree, node * 2, left, mid) + initSegmentTree(arr, segmentTree, node * 2 + 1, mid + 1, right))
    return segmentTree[node]

def findSectionValue(segmentTree, node, left, right, start, end):
    if left > end or right < start:
        return 0
    if start <= left and right <= end:
        return segmentTree[node]

    mid = (left + right) // 2
    return (findSectionValue(segmentTree, node * 2, left, mid, start, end) + findSectionValue(segmentTree, node * 2 + 1, mid + 1, right, start, end))

def updateValue(segmentTree, node, left, right, target, value):
    if not (left <= target and target <= right):
        return
    segmentTree[node] += value
    if left == right:
        return

    mid = (left + right) // 2
    updateValue(segmentTree, node * 2, left, mid, target, value)
    updateValue(segmentTree, node * 2 + 1, mid + 1, right, target, value)


def solution():
    N, M = map(int, sys.stdin.readline().split())

    arr = [0] * N

    height = int(math.ceil(math.log2(N)))
    treeSize = 1 << (height + 1)

    segmentTree = [0] * treeSize
    initSegmentTree(arr, segmentTree, 1, 0, N-1)

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        if a == 1:
            arr[b-1] += c
            updateValue(segmentTree, 1, 0, N-1, b-1, c)
        else:
            print(findSectionValue(segmentTree, 1, 0, N-1, b-1, c-1))

solution()