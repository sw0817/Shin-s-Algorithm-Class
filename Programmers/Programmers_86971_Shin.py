from collections import deque

adj = []
visited = []
children = []


def dfs(v):
    cnt = 1
    for nv in adj[v]:
        if not visited[nv]:
            visited[nv] = 1
            cnt += dfs(nv)
    children[v] = cnt
    return cnt


def solution(n, wires):
    global adj, children, visited

    answer = n - 1
    v = 0
    adj = [[] for _ in range(n + 1)]
    for s, e in wires:
        adj[s].append(e)
        adj[e].append(s)

    visited = [0] * (n + 1)
    queue = deque()
    w = wires[0][0]
    queue.append(w)
    visited[w] = 1
    while queue:
        w = queue.popleft()
        for nw in adj[w]:
            if not visited[nw]:
                visited[nw] = 1
                queue.append(nw)
        v = w

    children = [0] * (n + 1)
    visited = [0] * (n + 1)

    dfs(v)

    for cnt in children:
        answer = min(answer, abs(n - (cnt * 2)))

    return answer