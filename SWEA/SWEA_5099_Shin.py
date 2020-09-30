# SWEA 5099 피자 굽기
# SWEA 5099

# Created by sw0817 on 2020. 09. 30..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


from collections import deque


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    Q = deque()
    a = 1
    result = 0
    visited = [0] * M
    index = deque([-1] * N)
    while 0 in visited:
        for i in range(M):
            if len(Q) == N:
                break
            if visited[i] == 0:
                Q.append(Ci[i])
                visited[i] = 1
                for j in range(N):
                    if index[j] == -1:
                        index[j] = i
                        break

        if 0 in visited:
            a = 1
            while a != 0:
                a = Q.popleft() // 2
                if a == 0:
                    result = index[0]
                    index.popleft()
                    index.append(-1)
                else:
                    Q.append(a)
                    index.append(index.popleft())

    while len(Q) != 0:
        a = Q.popleft() // 2
        if a == 0:
            result = index[0]
            index.popleft()
        else:
            Q.append(a)
            index.append(index.popleft())

    print('#{} {}'.format(tc, result+1))
