# 백준 3003 킹, 퀸, 룩, 비숍, 나이트, 폰
# Baekjoon 3003

# Created by sw0817 on 2022. 10. 20..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/3003

print(*list([1, 1, 2, 2, 2, 8][i] - n for i, n in enumerate(list(map(int, input().split())))))