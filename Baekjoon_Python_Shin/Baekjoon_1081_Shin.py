# 백준 1081 합
# Baekjoon 1081

# Created by sw0817 on 2021. 08. 03..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1081

def cal(n):
    nums = [0] * 10
    if n <= 0:
        return 0
    # base
    i = 1
    left = 1
    right = n
    result = 0

    while left <= right:
        while right % 10 != 9 and left <= right:
            temp = right
            while temp:
                nums[temp % 10] += i
                temp //= 10
            right -= 1

        if right < left:
            break

        while left % 10 != 0 and left <= right:
            temp = left
            nums[temp % 10] += i
            left += 1

        left = 1
        right //= 10

        for j in range(10):
            nums[j] += (right-left+1) * i

        i *= 10

    for i in range(10):
        result += nums[i] * i

    return result


L, U = map(int, input().split())

# U 까지 합을 구하고, L-1 까지 합을 뺀다.
print(cal(U) - cal(L-1))