# 백준 2252 줄 세우기
# Baekjoon 2252

# Created by sw0817 on 2021. 02. 09..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2252

from _collections import deque

# 학생 수, 비교 수
N, M = map(int, input().split())

# 학생 번호가 1부터니까 1개 더
# 내 앞에 있는 학생 수
num_front = [0] * (N+1)

# 내 뒤에 있는 학생들 번호
back_of_ = [[] for _ in range(N+1)]

for _ in range(M):
    # A가 앞 B가 뒤
    A, B = map(int, input().split())
    # B앞에 학생 수 += 1
    num_front[B] += 1
    # A뒤에 B추가
    back_of_[A].append(B)

queue = deque()

for i in range(1, N+1):
    # 학생이 앞에 아무도 없는 애들부터 앞 줄
    if not num_front[i]:
        queue.append(i)

while queue:
    # 맨 앞 줄 학생부터 뽑아서
    front = queue.popleft()
    # 걔네 뒤에 있는 애들
    for back in back_of_[front]:
        # 큐에서 뽑힌 애 줄 서니까 앞에 있는 학생 수 -= 1
        num_front[back] -= 1
        # 더 이상 앞에 없으면 맨 앞 줄 세우기
        if not num_front[back]:
            queue.append(back)
    # 뽑힌 애 출력
    print(front, end=' ')