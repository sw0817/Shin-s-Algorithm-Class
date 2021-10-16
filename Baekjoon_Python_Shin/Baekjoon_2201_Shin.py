# 백준 2201 이친수
# Baekjoon 2201

# Created by sw0817 on 2021. 10. 16..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2201

K = int(input())
if K == 1:
    print(1)
elif K == 2:
    print(10)
else:
    length = [1] * 87
    ac_sum = [0] * 88
    ac_sum[0], ac_sum[1] = 1, 2
    idx = 0
    for i in range(2, 87):
        length[i] += ac_sum[i-2]
        ac_sum[i] = ac_sum[i-1] + length[i]
        if K <= ac_sum[i]:
            idx = i
            break

    result = 10 ** idx
    K -= ac_sum[idx-1] + 1

    while K:
        for i in range(87):
            if K <= ac_sum[i]:
                result += 10 ** (i)
                K -= ac_sum[i-1] + 1
                break

    print(result)