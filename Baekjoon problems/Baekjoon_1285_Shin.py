# 백준 1285 동전 뒤집기
# Baekjoon 1285

# Created by sw0817 on 2021. 09. 06..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1285

def check(bit):
    ret = 0
    for j in range(N):
        h_cnt = 0
        t_cnt = 0

        for i in range(N):
            if ((bit >> i) & 1) == 1:
                if arr[i][j] == 'H':
                    t_cnt += 1
                else:
                    h_cnt += 1
            else:
                if arr[i][j] == 'H':
                    h_cnt += 1
                else:
                    t_cnt += 1

        ret += min(h_cnt, t_cnt)

    return ret


N = int(input())
arr = [list(input()) for _ in range(N)]

result = 987654321
row_bit = 1 << N
for i in range(row_bit):
    result = min(result, check(i))

print(result)