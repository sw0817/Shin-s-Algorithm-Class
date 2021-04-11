# 백준 1101 스티커 정리 1
# Baekjoon 1101

# Created by sw0817 on 2021. 04. 11..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1101

N, M = map(int, input().split())
result = 999999

info = [list(map(int, input().split())) for _ in range(N)]

# i번 박스를 조커박스로 결정
for i in range(N):

    # m번 색만 가진 박스의 수
    color = [0] * M

    # 옮겨야 하는 횟수
    cnt = 0

    # 모든 박스 중 조커 박스가 아닌 박스만 조사
    for j in range(N):
        if j != i:

            # 어떤 색이 있으면 stack에 넣는다.
            stack = []
            for k in range(M):
                if info[j][k] != 0:
                    stack.append(k)

                    # 들어간 색이 여러개면 스티커는 모두 조커박스로
                    if 1 < len(stack):
                        cnt += 1
                        break

            # 한 가지 색만 가지고 있다면 그 색이 무엇인지 체크
            if len(stack) == 1:
                idx = stack.pop()
                color[idx] += 1

    # 모든 색에 대해 그 색만 가진 박스 하나로 나머지 다 모음
    for j in range(M):
        if 1 < color[j]:
            cnt += color[j] - 1

    # 옮긴 횟수 정리
    if cnt < result:
        result = cnt

print(result)
