def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    d = -30001
    for s, e in routes:
        if e < s:
            s, e = e, s
        if d < s:
            answer += 1
            d = e

    return answer