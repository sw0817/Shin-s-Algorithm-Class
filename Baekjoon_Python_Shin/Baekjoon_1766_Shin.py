# 백준 1766 문제집
# Baekjoon 1766

# Created by sw0817 on 2021. 08. 18..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1766

class MinHeap:
    def __init__(self, A):
        # 0번 index는 비운다.
        self.queue = [None] + A[:]
        for i in range(len(self.queue)//2, 0, -1):
            self.minHeapify(i)

    @staticmethod
    def parent(index):
        return index//2

    def insert(self, n):
        self.queue.append(n)
        # 마지막 idx
        i = len(self.queue)-1
        # root로 올 때까지 부모와 비교하며 더 작으면 바꿔주고 반복
        while 1 < i:
            parent = self.parent(i)
            if self.queue[i] < self.queue[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def delete(self):
        if len(self.queue) == 1:
            return 0
        # 마지막 원소와 root를 바꿔주고
        self.swap(1, len(self.queue)-1)
        # 마지막 원소를 제거
        n = self.queue.pop(len(self.queue)-1)
        # root에서 heapify 시작
        self.minHeapify(1)
        return n

    @staticmethod
    def leftchild(index):
        return index*2

    @staticmethod
    def rightchild(index):
        return index*2+1

    def minHeapify(self, i):
        left = self.leftchild(i)
        right = self.rightchild(i)
        # 우선 자신을 가장 작은 것으로 놓고
        smallest = i
        # 왼쪽 자식이 존재하고 가장 작은 것보다 작으면
        if left <= len(self.queue)-1 and self.queue[left] < self.queue[smallest]:
            smallest = left
        if right <= len(self.queue)-1 and self.queue[right] < self.queue[smallest]:
            smallest = right
        if smallest != i:
            self.swap(i, smallest)
            self.minHeapify(smallest)

    def swap(self, i, smallest):
        self.queue[i], self.queue[smallest] = self.queue[smallest], self.queue[i]


# 위상 정렬
def topologySort():
    queue = MinHeap([])
    for i in range(1, N+1):
        # 진입차수가 0
        if inDegree[i] == 0:
            queue.insert(i)

    while 1 < len(queue.queue):
        cur = queue.delete()
        print(cur, end=' ')
        for i in adj[cur]:
            # cur로부터 나가는 간선 제거
            inDegree[i] -= 1
            if inDegree[i] == 0:
                queue.insert(i)


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

topologySort()