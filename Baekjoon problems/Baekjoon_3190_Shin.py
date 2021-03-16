# 백준 3190 뱀
# Baekjoon 3190

# Created by sw0817 on 2021. 03. 16..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/3190

from _collections import deque

# 우하좌상(시계방향), 처음은 우
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir = 0

N = int(input())
K = int(input())

# 뱀 위치 배열, 시작점
snake = deque()
snake.append((0, 0))

# 움직일때마다 사과 있는지 확인할거니까 set 으로
apple = set()
for _ in range(K):
    r, c = map(int, input().split())
    # 나는 0부터 좌표 쓸거임
    apple.add((r-1, c-1))

# 움직임 하나 받을때마다 하면 예외처리 까다로우니 미리 다 받기
movement = deque()
L = int(input())
for _ in range(L):
    T, D = list(map(str, input().split()))
    T = int(T)
    movement.append((T, D))

# 벽에 부딛히든 자기 부딛힐때까지 갈 수 있는 마지막 움직임
movement.append((10101, 101))

# 초기값
t = 0
r, c = 0, 0
okay = True

# 10000번은 적은 횟수임. t를 1씩 늘려도 무방
while movement and okay:
    T, D = movement.popleft()
    for i in range(t, T):
        t += 1
        dr, dc = move[dir]
        r, c = r + dr, c + dc

        # 벽에 부딛히면 끝
        if r < 0 or N <= r or c < 0 or N <= c:
            okay = False
            break

        # 사과 먹으면 사과배열에서 제거
        if (r, c) in apple:
            apple.remove((r, c))

        else:
            # 이 부분이 납득은 안 되는데 움직이는 곳에 꼬리 마지막이 있어도 종료임(테케 3번)
            # 그래서 먼저 확인해주고
            if (r, c) in snake:
                okay = False
                break

            # 꼬리 끝 자르기
            snake.popleft()

        # 머리 움직인 부분 추가
        snake.append((r, c))

    # for 문 다 돌고 방향 변경
    if D == 'D':
        dir = (dir + 1) % 4
    else:
        dir = (dir - 1) % 4

print(t)