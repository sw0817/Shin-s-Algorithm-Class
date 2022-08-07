import math


def solution(n, costs):
    answer = 0

    adj = [[] for _ in range(n)]
    for s, e, c in costs:
        adj[s].append([e, c])
        adj[e].append([s, c])

    visited = [1] + [0] * (n - 1)

    cur_c = math.inf
    cur_idx = n

    for _ in range(n - 1):
        for i in range(n):
            if visited[i]:
                for v, c in adj[i]:
                    if not visited[v]:
                        if c < cur_c:
                            cur_idx = v
                            cur_c = c
        answer += cur_c
        visited[cur_idx] = 1
        cur_c = math.inf
        cur_idx = n

    return answer