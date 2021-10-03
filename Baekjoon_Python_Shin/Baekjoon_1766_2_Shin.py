# 백준 1766 문제집
# Baekjoon 1766

# Created by sw0817 on 2021. 08. 18..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1766

def minHeap(lst):
    queue = [None] + lst[:]
    for i in range(len(queue)//2, 0, -1):
        minHeapify(i)
    return queue


def parent(idx):
    return idx // 2


def leftchild(index):
    return index*2


def rightchild(index):
    return index*2+1


def insert(n):
    queue.append(n)
    i = len(queue)-1
    while 1 < i:
        p = parent(i)
        if queue[i] < queue[p]:
            swap(i, p)
            i = p
        else:
            break


def swap(i, p):
    queue[i], queue[p] = queue[p], queue[i]


def delete():
    if len(queue) == 1:
        return 0
    swap(1, len(queue)-1)
    n = queue.pop(len(queue)-1)
    minHeapify(1)
    return n


def minHeapify(i):
    left = leftchild(i)
    right = rightchild(i)
    smallest = i

    if left <= len(queue) - 1 and queue[left] < queue[smallest]:
        smallest = left
    if right <= len(queue) - 1 and queue[right] < queue[smallest]:
        smallest = right
    if smallest != i:
        swap(i, smallest)
        minHeapify(smallest)


# 위상 정렬
def topologySort():

    for i in range(1, N+1):
        # 진입차수가 0
        if inDegree[i] == 0:
            insert(i)

    while 1 < len(queue):
        cur = delete()
        print(cur, end=' ')
        for i in adj[cur]:
            # cur로부터 나가는 간선 제거
            inDegree[i] -= 1
            if inDegree[i] == 0:
                insert(i)


N, M = map(int, input().split())
# 인접 리스트
adj = [[] for _ in range(N+1)]
# 진입차수
inDegree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    # A는 B보다 빨리 풀어야 함
    adj[A].append(B)
    # B를 풀기 전 몇 개의 문제를 풀어야 하는지(진입차수)
    inDegree[B] += 1

queue = minHeap([])
topologySort()