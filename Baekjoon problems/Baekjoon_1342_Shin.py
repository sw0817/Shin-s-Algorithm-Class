# 백준 1342 행운의 문자열
# Baekjoon 1342

# Created by sw0817 on 2021. 09. 13..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1342

def dfs(d, word):
    global cnt
    if d == l:
        cnt += 1
        return

    for w in w_set:
        idx = ord(w) - ord('a')
        if not alps[idx]:
            continue

        if word and word[-1] == w:
            continue

        alps[idx] -= 1
        dfs(d + 1, word + w)
        alps[idx] += 1


word = input()
alps = [0] * 26
l = len(word)
cnt = 0
w_set = set()

for w in word:
    alps[ord(w) - ord('a')] += 1
    w_set.add(w)

dfs(0, '')
print(cnt)