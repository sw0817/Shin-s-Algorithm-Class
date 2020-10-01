# SWEA 5097 회전
# SWEA 5097

# Created by sw0817 on 2020. 10. 01..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


from collections import deque


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    Q = deque()
    Ns = list(map(int, input().split()))
    for i in range(len(Ns)):
        Q.append(Ns[i])
    for i in range(M):
        Q.append(Q.popleft())
    print('#{} {}'.format(tc, Q.popleft()))

