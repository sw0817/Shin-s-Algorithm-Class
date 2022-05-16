from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(place):
    visited = [[0] * 5 for _ in range(5)]
    queue = deque()
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                queue.append((i, j))

    while queue:
        r, c = queue.popleft()
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5 and not place[nr][nc] == 'X':
                if place[nr][nc] == 'P' or visited[nr][nc]:
                    return 0
                visited[nr][nc] = 1

    return 1


def solution(places):
    answer = []
    for i in range(5):
        answer.append(bfs(places[i]))

    return answer