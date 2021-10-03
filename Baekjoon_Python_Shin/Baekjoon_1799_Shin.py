# 백준 1799 비숍
# Baekjoon 1799

# Created by sw0817 on 2021. 08. 31..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1799

def dfs(r, c, cnt):
    # 비숍의 개수 갱신
    answer[flag] = max(answer[flag], cnt)

    # 다음 행 검사
    if N <= c:
        r += 1
        # 행이 바뀌면 시작 위치 달라짐
        c = flag ^ (r % 2)

    # 모든 행 검사 후 종료
    if N <= r:
        return

    # 해당 위치가 가능한지 확인
    if arr[r][c] and left[r+c] == 0 and right[r-c+N] == 0:
        left[r+c] = right[r-c+N] = 1
        dfs(r, c+2, cnt+1)
        left[r+c] = right[r-c+N] = 0

    # 다음 위치 검사
    dfs(r, c+2, cnt)


N = int(input())
answer = [0] * 2
# 비숍의 범위가 겹치는지 나타내는 변수, 값이 1이면 다른 비숍과 범위가 겹쳐 위치시킬 수 없음.
# 좌 하단 방향의 대각선
left = [0] * 21
# 우 하단 방향의 대각선
right = [0] * 21
# 흑과 백 구분 변수
flag = 0
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

# 흑색 칸 검사
dfs(0, 0, 0)
flag = 1
# 백색 칸 검사
dfs(0, 1, 0)

print(answer[0]+answer[1])