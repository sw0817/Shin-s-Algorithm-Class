# 백준 2550 전구
# Baekjoon 2550

# Created by sw0817 on 2021. 08. 04..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2550

N = int(input())
switches = list(map(int, input().split()))
lights = list(map(int, input().split()))

# LIS











# backtracking = [0] * N
# used = set()
# result = 0
# answer = []
# for i in range(N):
#     s = switches[i]
#     if s in used:
#         continue
#     temp = [s]
#     cnt = 1
#     low = lights.index(s)
#     for j in range(i+1, N):
#         s = switches[j]
#         if low < lights.index(s):
#             if backtracking[s-1] < cnt:
#                 backtracking[s-1] = cnt
#             else:
#                 continue
#             temp.append(s)
#             used.add(s)
#             cnt += 1
#             low = lights.index(s)
#
#     if result < cnt:
#         answer = temp
#         result = cnt
#
# print(result)
# print(*sorted(answer))
#
# # 실패코드