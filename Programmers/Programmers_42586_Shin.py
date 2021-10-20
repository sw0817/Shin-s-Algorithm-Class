def solution(progresses, speeds):
    answer = []

    l = len(speeds)

    remain = [0] * l
    for i in range(l):
        r = 100 - progresses[i]
        day = r // speeds[i]
        if r % speeds[i]:
            day += 1
        remain[i] = day

    cur = 0
    cnt = 0

    for i in range(l):
        if cnt == 0 or remain[i] <= cur:
            cur = max(cur, remain[i])
            cnt += 1
        else:
            cur = remain[i]
            answer.append(cnt)
            cnt = 1

    if cnt:
        answer.append(cnt)

    return answer