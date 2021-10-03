# 백준 2263 트리의 순회
# Baekjoon 2263

# Created by sw0817 on 2021. 07. 23..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2263

'''
15
8 7 10 2 15 5 12 3 9 4 14 1 6 11 13
8 10 7 15 12 5 2 9 14 4 6 13 11 1 3

13
8 7 10 2 12 5 3 9 4 1 6 11 13
8 10 7 12 5 2 9 4 6 13 11 1 3
'''


from sys import setrecursionlimit

def preOrder(inLeft, inRight, postLeft, postRight):
    # print()
    # print(inOrder[inLeft], inOrder[inRight], postOrder[postLeft], postOrder[postRight])
    if postLeft <= postRight and inLeft <= inRight:
        print()
        print(inOrder[inLeft], inOrder[inRight], postOrder[postLeft], postOrder[postRight])
        # print("hit")
        parent = postOrder[postRight]
        # print(parent, end=" ")
        pIdx = inPos[parent]
        # print(parent, pIdx)
        preOrder(inLeft, pIdx-1, postLeft, postLeft+pIdx-inLeft-1) # 부모 노드 기준 왼쪽
        preOrder(pIdx+1, inRight, postRight+pIdx-inRight, postRight-1)
    # else:
    #     print(inLeft, inRight, postLeft, postRight)

setrecursionlimit(10 ** 6)

N = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))
inPos = [0] * (N+1)
for idx, i in enumerate(inOrder):
    inPos[i] = idx
print(inPos)
preOrder(0, N-1, 0, N-1)