from collections import deque


def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            visited[i] = 1
            queue = deque()
            queue.append(i)
            while queue:
                v = queue.popleft()
                for j in range(n):
                    if not visited[j] and computers[v][j]:
                        visited[j] = 1
                        queue.append(j)

    return answer