# 백준 1843 방정식
# Baekjoon 1843

# Created by sw0817 on 2021. 02. 23..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1843

N = int(input())

B = C = 0

# A는 홀수 짝수에 따라 규칙이 나옵니다. 시간복잡도 O(1)
if N % 2:
    A = (N // 2) ** 2
else:
    A = (N // 2) * ((N // 2) - 1)

print(A)

# 1과 N은 반드시 약수이고 N이 1이여서 divisors = [1, 1]이 되어도 조건에 걸려서 상관없다.
divisors = [1, N]

# B랑 C를 동시에 구하기 위해 에라토스테네스의 체를 먼저 만들었습니다.
Eratosthenes = [True for i in range(N + 1)]

# 약수건 소수건 N의 제곱근까지만 for문을 돌아도 모두 구할 수 있습니다.
for i in range(2, int(N ** 0.5) + 1):

    # 소수를 확인하는 과정
    if Eratosthenes[i]:
        j = 2
        while i * j <= N:
            Eratosthenes[i * j] = False
            j += 1

    # 약수를 확인하는 과정
    if N % i == 0:
        divisors.append(i)

        # 이 조건을 안 주고 아래서 divisors = list(set(divisors)) 를 활용해도 무관하나 약간 시간손해.
        if i != N / i:
            divisors.append(N / i)

# 최종 소수 배열
prime_numbers = [i for i in range(2, N + 1) if Eratosthenes[i]]

# divisors를 크기순으로 정렬
divisors.sort()

# X <= Y 조건을 만족하며 Z까지 약수인 녀석 수
for i in range(len(divisors)):
    for j in range(i, len(divisors)):
        if divisors[i] + divisors[j] in divisors:
            B += 1

print(B)

# X <= Y 조건을 만족하며 Z까지 소수인 녀석 수
# 소수는 2를 제외하고 모두 홀수이기에, 소수 두 개의 합은 2가 포함되지 않으면 반드시 짝수
# 짝수는 2를 제외하고 모두 소수가 아니므로 확인할 필요가 없기 때문에 X는 반드시 2
for i in range(1, len(prime_numbers)):
    if prime_numbers[i] + 2 in prime_numbers:
        C += 1

print(C)