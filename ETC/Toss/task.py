def solution(tasks):
    answer = 0

    task = dict()
    for t in tasks:
        if t in task:
            task[t] += 1
        else:
            task[t] = 1

    for t in task:
        n = task[t]
        if n == 1:
            return -1
        if not n % 3:
            answer += n // 3
        else:
            answer += n // 3 + 1

    return answer