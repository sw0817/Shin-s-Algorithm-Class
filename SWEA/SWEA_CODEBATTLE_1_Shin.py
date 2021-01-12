# SWEA CODE BATTLE 오목 판정
# SWEA CODE BATTLE No. 1

# Created by sw0817 on 2021. 01. 12..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/talk/codeBattle/problemDetail.do?contestProbId=AXaSUPYqPYMDFASQ&categoryId=AXaTEYq6P2sDFASQ&categoryType=BATTLE

def check():
    for i in range(N):
        for j in range(N):
            if stones[i][j] == 'o' and 5 <= N-i:
                right = True
                for k in range(1, 5):
                    if stones[i+k][j] == '.':
                        right = False
                        break
                if right:
                    print('YES')
                    return
            if stones[i][j] == 'o' and 5 <= N-j:
                right = True
                for k in range(1, 5):
                    if stones[i][j+k] == '.':
                        right = False
                        break
                if right:
                    print('YES')
                    return
            if stones[i][j] == 'o' and 5 <= N-i and 5 <= N-j:
                right = True
                for k in range(1, 5):
                    if stones[i+k][j+k] == '.':
                        right = False
                        break
                if right:
                    print('YES')
                    return
            if stones[i][j] == 'o' and 4 <= i and 5 <= N-j:
                right = True
                for k in range(1, 5):
                    if stones[i-k][j+k] == '.':
                        right = False
                        break
                if right:
                    print('YES')
                    return
    print('NO')
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stones = [list(map(str, input())) for _ in range(N)]
    print('#{}'.format(tc), end=' ')
    check()
