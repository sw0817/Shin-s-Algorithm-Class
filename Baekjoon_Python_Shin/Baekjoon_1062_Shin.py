# 백준 1062 가르침
# Baekjoon 1062

# Created by sw0817 on 2020. 12. 17..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1062

def recur(idx, cnt, bit):
    global max_cnt
    if idx == 26 or cnt == 0:
        ret = 0
        for word in words:
            for w in word:
                if not bit & (1 << (ord(w) - 97)):
                    break
            else:
                ret += 1
        max_cnt = max(max_cnt, ret)
        return

    for i in range(idx, 26):
        if not bit & (1 << i):
            recur(i + 1, cnt-1, bit | (1 << i))


def solution(K):
    global max_cnt
    if K < 5:
        return 0
    basic = 0
    for alp in ['a', 'c', 't', 'i', 'n']:
        basic |= (1 << (ord(alp) - 97))
    K -= 5
    for i in range(26):
        recur(0, K, basic)
    return max_cnt


N, K = map(int, input().split())
words = []
for _ in range(N):
    word = input()
    word = set(word)
    words.append(word)
max_cnt = 0
print(solution(K))

# 비트마스킹 풀이도 시간초과