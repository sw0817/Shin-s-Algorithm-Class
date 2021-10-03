# 백준 1644 소수의 연속합
# Baekjoon 1644

# Created by sw0817 on 2021. 07. 03..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1644

N = int(input())
Eratos = [True] * (N+1)
# N을 제외한 N의 최대 약수
M = int(N ** 0.5)
for i in range(2, M+1):
    if Eratos[i]:
        for j in range(i*2, N+1, i):
            Eratos[j] = False

prime = [i for i in range(2, N+1) if Eratos[i]]

l = len(prime)
cnt = 0
start = 0
end = 0
if prime:
    num = prime[0]

    while start <= end:
        if num < N:
            end += 1
            if end < l:
                num += prime[end]
            else:
                break
        else:
            if num == N:
                cnt += 1
            num -= prime[start]
            start += 1

print(cnt)
