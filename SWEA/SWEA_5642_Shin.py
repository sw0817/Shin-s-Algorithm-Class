# SWEA 5642 합
# SWEA 5642

# Created by sw0817 on 2020. 12. 20..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXQm2SqdxkDFAUo&categoryId=AWXQm2SqdxkDFAUo&categoryType=CODE

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    result = -999999999
    max_num = -99999999
    sub_sum = 0
    for i in range(N):
        if max_num < nums[i]:
            max_num = nums[i]
        sub_sum += nums[i]
        if sub_sum < 0:
            sub_sum = 0
        else:
            if result < sub_sum:
                result = sub_sum

    if max_num <= 0:
        print('#{} {}'.format(tc, max_num))
        continue

    print('#{} {}'.format(tc, result))