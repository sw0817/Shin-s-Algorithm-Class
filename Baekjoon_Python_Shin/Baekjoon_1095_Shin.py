# 백준 1095 마법의 구슬
# Baekjoon 1095

# Created by sw0817 on 2021. 09. 21..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1095

def cal(num, flag):
    global decimal_cnt
    for i in range(decimal_size):
        n = decimal_list[i]
        temp = 0
        while num >= n:
            temp += num // n
            n *= decimal_list[i]
        decimal_cnt[i] += temp if flag else -temp


def check():
    for num in range(M, 0, -1):
        temp = num
        index = 0
        cnt = 0
        flag = True
        while temp > 1:
            if temp % decimal_list[index] == 0:
                temp //= decimal_list[index]
                cnt += 1
                if cnt > decimal_cnt[index]:
                    flag = False
                    break
            else:
                cnt = 0
                index += 1
        if flag:
            return num
    return -1


S, F, M = map(int, input().split())

decimal_list = []
decimal = [True] * (M+1)
for i in range(2, M+1):
    if decimal[i]:
        decimal_list.append(i)
        for j in range(i+i, M+1, i):
            decimal[j] = False

decimal_size = len(decimal_list)
decimal_cnt = [0] * decimal_size
cal(S+F, True)
cal(S, False)
cal(F, False)

print(check())