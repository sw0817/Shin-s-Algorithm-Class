# SWEA 4065 [Professional] LCS
# SWEA 4065

# Created by sw0817 on 2021. 04. 20..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    l1 = len(str1)
    l2 = len(str2)
    dp = [[0] * (l2+1) for _ in range(l1+1)]
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # for row in dp:
    #     print(row)
    print('#{} {}'.format(tc, dp[l1][l2]))

