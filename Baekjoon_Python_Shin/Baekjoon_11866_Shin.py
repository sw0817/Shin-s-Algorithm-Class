# 백준 11866 요세푸스 문제 0
# Baekjoon 11866

# Created by sw0817 on 2022. 03. 15..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11866

from collections import deque

N, K = map(int, input().split())
queue = deque()
for i in range(1, N+1):
    queue.append(i)

cnt = 0
result = "<"

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    result += str(queue.popleft())
    cnt += 1
    if cnt < N:
        result += ", "

result += ">"
print(result)