# 백준 1713 후보 추천하기
# Baekjoon 1713

# Created by sw0817 on 2021. 11. 15..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1713

N = int(input())
P = int(input())
P_list = list(map(int, input().split()))

cnt_list = [[-1, 0] for _ in range(101)]
last_set = set()

for i in range(P):
    n = P_list[i]
    if not n in last_set and N == len(last_set):
        cur = N+1
        cnt = P+1
        turn = P+1
        for idx in last_set:
            if cnt_list[idx][1] < cnt:
                cnt = cnt_list[idx][1]
                turn = cnt_list[idx][0]
                cur = idx
            elif cnt_list[idx][1] == cnt and cnt_list[idx][0] < turn:
                turn = cnt_list[idx][0]
                cur = idx
        last_set.discard(cur)
        cnt_list[cur][1] = 0
    cnt_list[n][1] += 1
    if not n in last_set:
        cnt_list[n][0] = i
        last_set.add(n)


result = list(last_set)
result.sort()
print(*result)
