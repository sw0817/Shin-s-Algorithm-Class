# SWEA 4008 숫자 만들기
# SWEA 4008

# Created by sw0817 on 2020. 11. 07..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH&categoryId=AWIeRZV6kBUDFAVH&categoryType=CODE


def cal(n, num):
    global max_num, min_num

    if n == N-1:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    for i in range(4):
        if operater[i] > 0:
            operater[i] -= 1
            num2 = num
            if i == 0:
                num2 += nums[n+1]
            elif i == 1:
                num2 -= nums[n+1]
            elif i == 2:
                num2 *= nums[n+1]
            else:
                if nums[n+1] != 0:
                    num2 = int(num / nums[n+1])
                else:
                    return

            cal(n+1, num2)
            operater[i] += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    operater = list(map(int, input().split())) # + - * /
    nums = list(map(int, input().split()))
    max_num = (999 ** 3) * (-1)
    min_num = (999 ** 3)
    cal(0, nums[0])
    result = max_num - min_num
    print('#{} {}'.format(tc, result))