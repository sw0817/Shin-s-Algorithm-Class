def solution(N, stages):
    answer = []

    l = len(stages)
    reached = dict()
    for i in range(1, N + 2):
        reached[i] = 0

    for s in stages:
        reached[s] += 1

    result = []
    cur = reached[N + 1]
    for i in range(N, 0, -1):
        temp = reached[i]
        if not temp + cur:
            result.append([i, 0])
        else:
            result.append([i, temp / (temp + cur)])
        cur += temp

    result.sort(key=lambda x: [-x[1], x[0]])

    for i, v in result:
        answer.append(i)

    return answer