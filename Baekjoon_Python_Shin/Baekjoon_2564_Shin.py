# 백준 2564 최소 힙
# Baekjoon 2564

# Created by sw0817 on 2020. 10. 16..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2564


def move(n, N):
    global x, y
    if arr[n][0] == arr[N][0]:
        return abs(arr[n][1] - arr[N][1])
    elif arr[n][1] == arr[N][1]:
        return abs(arr[n][0] - arr[N][0])
    else:
        move_c = arr[n][0] + arr[N][0]
        if move_c > y:
            move_c = 2 * y - move_c
        move_r = arr[n][1] + arr[N][1]
        if move_r > x:
            move_r = 2 * x - move_r
    return move_c + move_r


x, y = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N+1)]
ans = 0
for i in range(N+1):
    if arr[i][0] == 1:
        arr[i][0] = 0
    elif arr[i][0] == 2:
        arr[i][0] = y
    elif arr[i][0] == 3:
        arr[i][0], arr[i][1] = arr[i][1], 0
    elif arr[i][0] == 4:
        arr[i][0], arr[i][1] = arr[i][1], x
for i in range(N):
    ans += move(i, N)

print(arr)
print(ans)