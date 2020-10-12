# SWEA 5177 이진 힙
# SWEA 5177

# Created by sw0817 on 2020. 10. 12..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def heap_push(n):
    global last_idx
    last_idx += 1
    heap[last_idx] = n
    cur = last_idx
    parent = cur // 2
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0] * (N + 1)
    temp = list(map(int, input().split()))
    last_idx = 0
    for i in range(N):
        heap_push(temp[i])
    result = 0
    while N != 0:
        N = N // 2
        result += heap[N]

    print('#{} {}'.format(tc, result))