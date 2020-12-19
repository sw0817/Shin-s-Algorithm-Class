# 백준 1525 퍼즐
# Baekjoon 1525

# Created by sw0817 on 2020. 12. 19..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1525

from collections import deque

next = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs():
    queue = deque()
    queue.append(key)
    dist[key] = 0

    while queue:
        num = queue.popleft()
        if num == '123456780':
            return dist[num]

        idx = num.find('0')
        r, c = idx%3, idx//3

        for dr, dc in next:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                nidx = nr + (nc * 3)
                nnum = list(num)
                nnum[idx], nnum[nidx] = nnum[nidx], nnum[idx]
                nums = ''.join(nnum)

                if not dist.get(nums):
                    dist[nums] = dist[num] + 1
                    queue.append(nums)

    return -1

dist = dict()
key = ''

for i in range(3):
    key += input().replace(' ', '')

print(bfs())