# 백준 17472 다리 만들기 2
# Baekjoon 17472

# Created by sw0817 on 2021. 02. 03..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/17472

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def final():
    if impossible:
        print(-1)
        return

    for i in range(cnt - 2):
        if visited[i] == 0:
            print(-1)
            return

    print(result)


# 다른 섬과의 거리를 측정
def measure(i, j):
    for dr, dc in moves:
        length = 0
        nr = dr + i
        nc = dc + j
        if nr < 0 or nc < 0 or N <= nr or M <= nc:
            continue

        # 바다로 나갔다면
        while arr[nr][nc] == 0:
            nr += dr
            nc += dc

            # 맵 밖이면 탈출
            if nr == N or nc == M or nr == -1 or nc == -1:
                break

            # 거리 증가
            length += 1

            # 다른 섬이고, 거리가 2 이상 즉 다리를 놓을 수 있고,
            if arr[nr][nc] != arr[i][j] and arr[nr][nc] > 0:
                if length < 2:
                    break

                # 두 섬이 이어진적이 없거나, 기존에 다른 위치에서 이은 다리보다 짧은 길이라면 갱신하고 두 섬은 mst에 포함
                elif adj[arr[i][j] - 2][arr[nr][nc] - 2] == 0 or adj[arr[i][j] - 2][arr[nr][nc] - 2] > length:
                    adj[arr[i][j] - 2][arr[nr][nc] - 2] = length
                    visited[arr[i][j] - 2] = visited[arr[nr][nc] - 2] = 1
                break


# 연결되어 있는 땅을 하나의 섬으로 표시
def classfy(i, j):
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1
    queue = [(i, j)]
    arr[i][j] = cnt
    while queue:
        r, c = queue.pop(0)
        for dr, dc in moves:
            nr = dr + r
            nc = dc + c
            if nr < 0 or nc < 0 or N <= nr or M <= nc or visited[nr][nc] == 1:
                continue
            if arr[nr][nc] == 1:
                visited[nr][nc] = 1
                arr[nr][nc] = cnt
                queue.append((nr, nc))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 0과 1로 나타나 있는 섬 정보를 통해 2 이상의 숫자로 섬을 분류한다.
cnt = 2
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            classfy(i, j)
            cnt += 1

# 섬 갯수만큼 인접 배열을 만든다.
adj = [[0] * (cnt - 2) for _ in range(cnt - 2)]

# mst를 위해 선택 배열 만들기
visited = [0] * (cnt - 2)

# 바다가 아닌 섬에서 다른 섬과의 거리 측정
for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            measure(i, j)

# 이어진 다리들에 대해 mst를 구한다.
INF = 101
key = [INF] * (cnt - 2)
mst = [False] * (cnt - 2)

key[0] = 0
prims = 0
result = 0
impossible = 0
while prims <= cnt - 3:
    minV = INF
    minidx = 0
    for i in range(cnt - 2):
        if not mst[i] and minV > key[i]:
            minV = key[i]
            minidx = i

    mst[minidx] = True
    if minV == INF:
        impossible = 1
        break
    result += minV
    prims += 1

    for w in range(cnt - 2):
        if adj[minidx][w] > 0 and not mst[w] and key[w] > adj[minidx][w]:
            key[w] = adj[minidx][w]

# 이어지지 못한 섬이 있다면 -1을 출력
final()

