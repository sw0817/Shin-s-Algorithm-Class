# 백준 2026 소풍
# Baekjoon 2026

# Created by sw0817 on 2021. 08. 08..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2026

from collections import deque

K, N, F = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(F):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

result = False
done = set()

for i in range(1, N+1):
    adj[i].sort()

for i in range(1, N+1):
    if i in done:
        continue
    temp = []
    nums = deque()
    nums.append(i)
    temp.append(i)
    done.add(i)
    while nums:
        n = nums.popleft()
        for nn in adj[n]:
            if not nn in done:
                c = True
                for check in temp:
                    if not check in adj[nn]:
                        c = False
                        break
                if not c:
                    continue
                done.add(nn)
                temp.append(nn)
                nums.append(nn)
    if K <= len(temp):
        result = True
        temp.sort()
        for i in range(K):
            print(temp[i])
        break
    else:
        for n in temp:
            done.remove(n)

if not result:
    print(-1)