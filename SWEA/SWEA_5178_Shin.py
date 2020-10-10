# SWEA 5178 노드의 합
# SWEA 5178

# Created by sw0817 on 2020. 10. 10..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for i in range(M):
        leaf, num = map(int, input().split())
        tree[leaf] = num

    for i in range(N, 0, -1):
        if tree[i] == 0:
            if N > i*2:
                tree[i] = tree[i*2] + tree[i*2+1]
            else:
                tree[i] = tree[i*2]

    print('#{} {}'.format(tc, tree[L]))
