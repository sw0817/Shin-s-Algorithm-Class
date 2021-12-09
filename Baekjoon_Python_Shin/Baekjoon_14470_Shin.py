# 백준 14470 전자레인지
# Baekjoon 14470

# Created by sw0817 on 2021. 12. 09..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/14470

# 원래의 고기의 온도 (-100 <= A, A != 0)
A = int(input())
# 목표 온도 (1 <= B <= 100, A < B)
B = int(input())
# 얼어있는 고기 1'C 데우는데 걸리는 시간
C = int(input())
# 얼어있는 고기 해동하는데 걸리는 시간
D = int(input())
# 얼어있지 않은 고기를 1'C 데우는데 걸리는 시간
E = int(input())

t = 0

if A < 0:
    t += min(-A, B-A) * C
    A += min(-A, B-A)

if A == 0 and B:
    t += D

if A < B:
    t += (B-A) * E

print(t)