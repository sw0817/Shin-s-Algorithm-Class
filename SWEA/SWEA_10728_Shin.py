# SWEA 10728 수나열누기
# SWEA 10728

# Created by sw0817 on 2020. 10. 19..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXRSfaWq-igDFAXS&categoryId=AXRSfaWq-igDFAXS&categoryType=CODE


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = 0
    temp2 = 0
    temp_num = nums[0]

    while temp2 < N:
        min_num = nums[temp2]
        for i in range(temp2, N):
            if nums[i] > temp_num:
                temp_num = nums[i]
                temp2 = i
            elif nums[i] < min_num:
                break
        result += 1
        temp2 += 1

    print('#{} {}'.format(tc, result))