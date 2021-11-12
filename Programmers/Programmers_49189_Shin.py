from collections import deque

def solution(n, edge):
    answer = 0
    adj = [[] for _ in range(n + 1)]

    for s, e in edge:
        adj[s].append(e)
        adj[e].append(s)

    visited = [0] * (n + 1)
    visited[1] = 1
    queue = deque()
    queue.append(1)

    while queue:
        cnt = 0
        for _ in range(len(queue)):
            v = queue.popleft()
            cnt += 1
            for n_v in adj[v]:
                if not visited[n_v]:
                    visited[n_v] = 1
                    queue.append(n_v)
        answer = cnt

    return answer