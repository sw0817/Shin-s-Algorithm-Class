# 백준 2263 트리의 순회
# Baekjoon 2263

# Created by sw0817 on 2021. 07. 23..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2263

from sys import setrecursionlimit

def preOrder(inLeft, inRight, postLeft, postRight):
    # print(inOrder[inLeft], inOrder[inRight], postOrder[postLeft], postOrder[postRight])
    if postLeft <= postRight and inLeft <= inRight:
        parent = postOrder[postRight]
        print(parent, end=" ")
        pIdx = inPos[parent]
        preOrder(inLeft, pIdx-1, postLeft, postLeft+pIdx-inLeft-1) # 부모 노드 기준 왼쪽
        preOrder(pIdx+1, inRight, postRight+pIdx-inRight, postRight-1)


setrecursionlimit(10 ** 6)

N = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))
inPos = [0] * (N+1)
for idx, i in enumerate(inOrder):
    inPos[i] = idx
# print(inPos)
preOrder(0, N-1, 0, N-1)