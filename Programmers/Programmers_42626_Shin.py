import heapq


def solution(scoville, K):
    answer = 0
    l = len(scoville)

    heapq.heapify(scoville)
    while scoville[0] < K and 1 < l:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
        l -= 1

    if l == 1 and scoville[0] < K:
        answer = -1

    return answer