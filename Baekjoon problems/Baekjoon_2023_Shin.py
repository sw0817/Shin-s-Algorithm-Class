# 백준 2023 신기한 소수
# Baekjoon 2023

# Created by sw0817 on 2021. 08. 07..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2023

# 8자리는 10,000,000

# n = 10000000
# a = [True] * n
# primes = set()
# for i in range(2, int(n ** 0.5) + 1):
#     if a[i]:
#         primes.add(i)
#         for j in range(2*i, n, i):
#             a[j] = False
#
# N = int(input())
# for prime in primes:
#     if 10 ** (N-1) <= prime < 10 ** N:
#         check = True
#         p = str(prime)
#         for j in range(1, len(p)-1):
#             if not int(p[:j]) in primes:
#                 check = False
#                 break
#         if check:
#             print(p)

# 메모리 초과

def prime_check(num):
    # print(num)
    for i in range(2, int((int(num) ** 0.5)) + 1):
        # 소수가 아님
        if int(num) % i == 0:
            return False

    # 소수일 때
    # N자리수가 되면 출력
    if len(num) == N:
        print(num)
        return

    # nums 숫자들을 더해준다
    for i in nums:
        prime_check(num + i)


N = int(input())

prime_num = ['2', '3', '5', '7']

nums = ['1', '3', '7', '9']

for i in prime_num:
    prime_check(i)