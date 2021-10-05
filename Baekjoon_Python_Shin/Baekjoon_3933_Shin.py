# 백준 3933 라그랑주의 네 제곱수 정리
# Baekjoon 3933

# Created by sw0817 on 2021. 10. 05..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/3933

max_n = int((2 ** 15) ** 0.5)
nums = [i ** 2 for i in range(1, max_n+1)]

while True:
    n = int(input())
    idx = int(n ** 0.5)

    result = 0

    if n == 0:
        break

    i = 0
    while i < idx:
        if nums[i] == n:
            result += 1
            break

        j = i
        while j < idx:
            if nums[i] + nums[j] == n:
                result += 1
                break

            elif nums[i] + nums[j] > n:
                break

            k = j
            while k < idx:
                if nums[i] + nums[j] + nums[k] == n:
                    result += 1
                    break

                elif nums[i] + nums[j] + nums[k] > n:
                    break

                l = k
                while l < idx:
                    if nums[i] + nums[j] + nums[k] + nums[l] == n:
                        result += 1
                        break

                    elif nums[i] + nums[j] + nums[k] + nums[l] > n:
                        break

                    l += 1

                k += 1

            j += 1

        i += 1

    print(result)