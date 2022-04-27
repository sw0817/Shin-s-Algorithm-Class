from collections import deque
import math

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def solution(board):

    l = len(board)
    visited = [[[math.inf] * 4 for _ in range(l)] for _ in range(l)]
    visited[0][0] = [0, 0, 0, 0]

    queue = deque()
    for i in range(4):
        queue.append((0, 0, 0, i))
    while queue:
        r, c, cost, d = queue.popleft()
        for i in range(4):
            dr, dc = move[i]
            nr, nc = r + dr, c + dc
            if 0 <= nr < l and 0 <= nc < l and not board[nr][nc]:
                if d == i and cost + 100 < visited[nr][nc][i]:
                    queue.append((nr, nc, cost + 100, i))
                    visited[nr][nc][i] = cost + 100
                elif d != i and cost + 600 < visited[nr][nc][i]:
                    queue.append((nr, nc, cost + 600, i))
                    visited[nr][nc][i] = cost + 600

    return min(visited[l - 1][l - 1])