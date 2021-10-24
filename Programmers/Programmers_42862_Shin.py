def solution(n, lost, reserve):
    answer = 0

    status = [1] * (n + 2)
    status[0], status[n + 1] = 0, 0
    for i in lost:
        status[i] -= 1

    for i in reserve:
        status[i] += 1

    for i in range(1, n + 1):
        if status[i]:
            answer += 1
        else:
            if 1 < status[i - 1]:
                answer += 1
            elif 1 < status[i + 1]:
                status[i + 1] -= 1
                answer += 1

    return answer