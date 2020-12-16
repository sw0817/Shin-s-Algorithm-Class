# 백준 1062 가르침
# Baekjoon 1062

# Created by sw0817 on 2020. 12. 17..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1062

from itertools import combinations


basic = ['a', 'n', 't', 'i', 'c']
basic = list(set(basic))


def solve():
    if K < 5:
        print(0)
        return

    else:
        cnt = K - 5

        unknown = []
        for word in words:
            for letter in word:
                if not letter in basic:
                    unknown.append(letter)

        unknown = list(set(unknown))
        # print(unknown)
        # print(words)

        result = 0
        if len(unknown) <= cnt:
            result = N

        else:
            idxs = [i for i in range(len(unknown))]
            combs = combinations(idxs, cnt)
            for comb in combs:
                cnt = 0
                for idx in comb:
                    basic.append(unknown[idx])

                # print(basic)

                for i in range(len(words)):
                    if len(words)-i <= result:
                        break
                    cnt += 1
                    for letter in words[i]:
                        if not letter in basic:
                            cnt -= 1
                            break

                if result < cnt:
                    result = cnt

                if result == N:
                    break

                for idx in comb:
                    basic.remove(unknown[idx])

                # print(cnt)

        print(result)


N, K = map(int, input().split())

words = []

for i in range(N):
    words.append(list(set(list(input()))))

solve()

# 좀 더 고민해볼 것