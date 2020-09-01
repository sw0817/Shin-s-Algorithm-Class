# SWEA 6109 추억의 2048게임
# SWEA 6109

# Created by sw0817 on 2020. 09. 01..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWbrg9uabZsDFAWQ&categoryId=AWbrg9uabZsDFAWQ&categoryType=CODE


import copy

T = int(input())
for tc in range(1, T+1):
    n, di = input().split()
    N = int(n)
    G = [list(map(int, input().split())) for _ in range(N)]
    A = []

    if di == 'up':
        while A != G:
            A = copy.deepcopy(G)
            for j in range(N):
                for i in range(N-1):
                        if G[N-i-2][j] == 0:
                            G[N-i-2][j] = G[N-i-1][j]
                            G[N-i-1][j] = 0

        for j in range(N):
            visited = [0] * N
            for i in range(N - 1):
                if G[i][j] == G[i+1][j] and visited[i+1] == 0 and visited[i] == 0:
                    G[i][j] = 0
                    G[i+1][j] *= 2
                    visited[i+1] = 1
                    visited[i] = 1

        while A != G:
            A = copy.deepcopy(G)
            for j in range(N):
                for i in range(N-1):
                        if G[N-i-2][j] == 0:
                            G[N-i-2][j] = G[N-i-1][j]
                            G[N-i-1][j] = 0

        print('#{}'.format(tc))
        for i in range(N):
            print(" ".join(map(str, G[i])))

    elif di == 'down':
        while A != G:
            A = copy.deepcopy(G)
            for j in range(N):
                for i in range(N - 1):
                    if G[i+1][j] == 0:
                        G[i+1][j] = G[i][j]
                        G[i][j] = 0

        for j in range(N):
            visited = [0] * N
            for i in range(N - 1):
                if G[N-i-1][j] == G[N-i-2][j] and visited[N-i-2] == 0 and visited[N-i-1] == 0:
                    G[N-i-1][j] = 0
                    G[N-i-2][j] *= 2
                    visited[N-i-2] = 1
                    visited[N-i-1] = 1

        while A != G:
            A = copy.deepcopy(G)
            for j in range(N):
                for i in range(N - 1):
                    if G[i+1][j] == 0:
                        G[i+1][j] = G[i][j]
                        G[i][j] = 0

        print('#{}'.format(tc))
        for i in range(N):
            print(" ".join(map(str, G[i])))

    elif di == 'right':
        while A != G:
            A = copy.deepcopy(G)
            for j in range(N):
                for i in range(N - 1):
                    if G[j][i+1] == 0:
                        G[j][i+1] = G[j][i]
                        G[j][i] = 0

        for j in range(N):
            visited = [0] * N
            for i in range(N - 1):
                if G[j][N-i-1] == G[j][N-i-2] and visited[N-i-2] == 0 and visited[N-i-1] == 0:
                    G[j][N-i-1] = 0
                    G[j][N-i-2] *= 2
                    visited[N-i-2] = 1
                    visited[N-i-1] = 1

        while A != G:
            A = copy.deepcopy(G)
            for j in range(N):
                for i in range(N - 1):
                    if G[j][i+1] == 0:
                        G[j][i+1] = G[j][i]
                        G[j][i] = 0

        print('#{}'.format(tc))
        for i in range(N):
            print(" ".join(map(str, G[i])))

    elif di == 'left':
        while A != G:
            A = copy.deepcopy(G)
            for j in range(N):
                for i in range(N-1):
                        if G[j][N-i-2] == 0:
                            G[j][N-i-2] = G[j][N-i-1]
                            G[j][N-i-1] = 0

        for j in range(N):
            visited = [0] * N
            for i in range(N - 1):
                if G[j][i] == G[j][i+1] and visited[i+1] == 0 and visited[i] == 0:
                    G[j][i] = 0
                    G[j][i+1] *= 2
                    visited[i+1] = 1
                    visited[i] = 1

        while A != G:
            A = copy.deepcopy(G)
            for j in range(N):
                for i in range(N-1):
                        if G[j][N-i-2] == 0:
                            G[j][N-i-2] = G[j][N-i-1]
                            G[j][N-i-1] = 0

        print('#{}'.format(tc))
        for i in range(N):
            print(" ".join(map(str, G[i])))