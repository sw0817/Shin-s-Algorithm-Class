# 백준 1331 나이트 투어
# Baekjoon 1331

# Created by sw0817 on 2021. 12. 30..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1331

valid = True
visited = set()
first = input()
visited.add(first)
cur = first
for _ in range(35):
    nxt = input()
    if nxt in visited:
        valid = False
        cur = nxt
        continue
    visited.add(nxt)
    alp = abs(ord(cur[0]) - ord(nxt[0]))
    num = abs(int(cur[1]) - int(nxt[1]))
    cur = nxt
    if alp == 2 and num == 1 or alp == 1 and num == 2:
        continue
    else:
        valid = False

alp = abs(ord(cur[0]) - ord(first[0]))
num = abs(int(cur[1]) - int(first[1]))

if alp == 2 and num == 1 or alp == 1 and num == 2 and valid and len(visited) == 36:
    print('Valid')
else:
    print('Invalid')