# 백준 1897 토달기
# Baekjoon 1897

# Created by sw0817 on 2021. 11. 21..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1897

def recur(w, l_w):
    global result, ret

    if result < l_w-1:
        result = l_w-1
        ret = w

    if l_w == 80:
        return

    for target in words[l_w]:
        cnt = 0
        idx = 0
        for i in range(l_w-1):
            if target[i] != w[idx]:
                cnt += 1
                if cnt == 2:
                    break
            else:
                idx += 1

        if idx == l_w-2 and target[l_w-1] == w[idx] or idx == l_w-1 and not cnt:
            recur(target, l_w+1)


N, initial = map(str, input().split())
N = int(N)
L = len(initial)

words = [set() for _ in range(81)]
for _ in range(N):
    word = input()
    l = len(word)
    words[l].add(word)

result = 3
ret = initial
recur(initial, L+1)
print(ret)