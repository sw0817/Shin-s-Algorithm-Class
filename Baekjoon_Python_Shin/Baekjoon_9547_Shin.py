# 백준 9547 대통령 선거
# Baekjoon 9547

# Created by sw0817 on 2021. 11. 17..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/9547

def solution(C, V):
    people = [True] * (C + 1)
    V_list = []

    for _ in range(V):
        V_list.append(list(map(int, input().split())))

    for t in range(1, 3):
        v_s = [[0, i] for i in range(C + 1)]
        for vote in V_list:
            for i in range(C):
                n = vote[i]
                if people[n]:
                    v_s[n][0] += 1
                    if V / 2 < v_s[n][0]:
                        print(n, t)
                        return
                    break
        v_s.sort()
        for i in range(C - 1):
            people[v_s[i][1]] = False


T = int(input())
for _ in range(T):
    C, V = map(int, input().split())
    solution(C, V)