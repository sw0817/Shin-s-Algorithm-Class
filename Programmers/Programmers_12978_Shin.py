import heapq


def solution(N, road, K):
    INF = int(1e9)
    answer = INF
    adj = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    for s, e, d in road:
        adj[s].append((e, d))
        adj[e].append((s, d))

    queue = []
    heapq.heappush(queue, (0, 1))
    distance[1] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    answer = 0
    for i in range(1, N + 1):
        if distance[i] <= K:
            answer += 1

    return answer