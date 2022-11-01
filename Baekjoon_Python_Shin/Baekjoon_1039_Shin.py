# 백준 1039 교환
# Baekjoon 1039

# Created by sw0817 on 2022. 11. 01..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1039

from collections import deque
from itertools import combinations
import copy


def bfs():
    c = set()
    ret = 0
    l = len(q)
    while l:
        x = q.popleft()
        l = list(str(x))
        for i, j in d:
            s = copy.deepcopy(l)
            temp_i, temp_j = s[i], s[j]
            s[i], s[j] = temp_j, temp_i
            if s[0] == '0':
                continue

            nx = int(''.join(s))
            if nx not in c:
                ret = max(ret, nx)
                c.add(nx)
                q.append(nx)
        l -= 1
    return ret


N, K = map(int, input().split())
item = [i for i in range(len(str(N)))]
d = list(combinations(item, 2))
q = deque()
q.append(N)

ans = 0
while K:
    ans = bfs()
    K -= 1
if not ans:
    print(-1)
else:
    print(ans)