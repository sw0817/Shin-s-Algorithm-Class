# SWEA 2819 격자판의 숫자 이어 붙이기
# SWEA 2819

# Created by sw0817 on 2020. 10. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(i, j, length, word):
    word = word + G[i][j]
    if length == 6:
        check.append(word)
        return
    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if nr < 0 or 3 < nr or nc < 0 or 3 < nc:
            continue
        else:
            dfs(nr, nc, length + 1, word)


T = int(input())
for tc in range(1, T+1):
    G = [list(map(str, input().split())) for _ in range(4)]
    check = []
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, '')
    check = set(check)
    print('#{} {}'.format(tc, len(check)))

