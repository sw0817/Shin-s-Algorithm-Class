from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    answer = 1
    queue = deque()
    queue.append((0, 0))
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if (r, c) == (n - 1, m - 1):
                return answer
            for dr, dc in move:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and maps[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
        answer += 1

    return -1