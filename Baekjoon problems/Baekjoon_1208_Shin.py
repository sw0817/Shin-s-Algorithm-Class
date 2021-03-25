# 백준 1208 부분수열의 합2
# Baekjoon 1208

# Created by sw0817 on 2021. 03. 25..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1208

from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))
result = 0
left = nums[:N//2]
right = nums[N//2:]
left_com, right_com = [], []

for i in range(N//2 + 1):
    for comb in combinations(left, i):
        left_com.append(sum(comb))
for i in range(N + 1 - N//2):
    for comb in combinations(right, i):
        right_com.append(sum(comb))

left_com.sort()
right_com.sort()

l_left = len(left_com)
l_right = len(right_com)
l_idx = 0
r_idx = l_right-1

while l_idx < l_left and 0 <= r_idx:
    sum_num = left_com[l_idx] + right_com[r_idx]
    if sum_num == S:
        l_num, r_num = 1, 1
        l_cur_idx = l_idx
        r_cur_idx = r_idx
        l_cur_idx += 1
        r_cur_idx -= 1
        while l_cur_idx < l_left and left_com[l_cur_idx] == left_com[l_idx]:
            l_num += 1
            l_cur_idx += 1
        while 0 <= r_cur_idx and right_com[r_cur_idx] == right_com[r_idx]:
            r_num += 1
            r_cur_idx -= 1

        l_idx = l_cur_idx
        r_idx = r_cur_idx

        result += l_num * r_num

    elif sum_num < S:
        l_idx += 1
    else:
        r_idx -= 1

if S == 0:
    result -= 1

print(result)