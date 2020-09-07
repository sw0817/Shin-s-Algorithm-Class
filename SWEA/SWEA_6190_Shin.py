# SWEA 6190 정곤이의 단조 증가하는 수
# SWEA 6190

# Created by sw0817 on 2020. 09. 07..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWcPjEuKAFgDFAU4&categoryId=AWcPjEuKAFgDFAU4&categoryType=CODE


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = list(map(int, input().split()))
    result = []
    for i in range(N-1, -1, -1):
        for j in range(i-1, -1, -1):
            num = M[i] * M[j]
            st_n = str(num)
            check = []
            for k in range(len(st_n)):
                check.append(int(st_n[k]))
            check_b = sorted(check)

            if check == check_b:
                result.append(num)
                break

    if len(result) == 0:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, max(result)))