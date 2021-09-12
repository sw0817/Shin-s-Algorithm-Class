import heapq

def solution(n, s, a, b, fares):
    answer = 0

    INF = int(1e9)
    adj = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    for start, end, fare in fares:
        adj[start].append((end, fare))
        adj[end].append((start, fare))

    queue = []
    heapq.heappush(queue, (0, a))
    distance[a] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    answer += distance[b]

    distance = [INF] * (n + 1)
    queue = []
    heapq.heappush(queue, (0, s))
    distance[s] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    answer += min(distance[a], distance[b])

    return answer

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))