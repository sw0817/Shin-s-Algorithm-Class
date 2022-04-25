from itertools import combinations


def solution(nums):
    answer = 0

    primes = [True] * 3001
    for i in range(2, int(3000 ** 0.5) + 1):
        if not primes[i]:
            continue

        for j in range(2 * i, 3001, i):
            primes[j] = False

    for comb in combinations(nums, 3):
        if primes[sum(comb)]:
            answer += 1

    return answer