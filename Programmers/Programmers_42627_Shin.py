import heapq

def solution(jobs):
    answer = 0
    l = len(jobs)
    jobs.sort(reverse=True)
    t = 0
    queue = []
    while jobs:
        if not queue:
            s, e = jobs.pop()
            if t <= s:
                answer += e
                t = s + e
            else:
                t += e
                answer += t - s
            while jobs and jobs[-1][0] < t:
                s, e = jobs.pop()
                heapq.heappush(queue, [e, s])
        if queue:
            while queue and queue[0][1] <= t:
                e, s = heapq.heappop(queue)
                t += e
                answer += t - s
                while jobs and jobs[-1][0] < t:
                    s, e = jobs.pop()
                    heapq.heappush(queue, [e, s])

    return answer // l

lst = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
print(solution(lst))