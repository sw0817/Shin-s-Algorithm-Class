def solution(gems):
    names = list(set(gems))
    have = dict()
    c = len(names)
    l = len(gems)
    if c == 1:
        return [1, 1]
    answer = [1, l]
    min_l = l
    for i in range(c):
        have[names[i]] = (0, i)

    visited = [0] * c
    s, e = 0, 0
    cnt, idx = have[gems[e]]
    visited[idx] = 1
    have[gems[e]] = (cnt + 1, idx)
    e += 1
    while e < l:
        if sum(visited) < c:
            cnt, idx = have[gems[e]]
            visited[idx] = 1
            have[gems[e]] = (cnt + 1, idx)
            e += 1
        else:
            cnt, idx = have[gems[s]]
            if e - s < min_l:
                min_l = e - s
                answer = [s + 1, e]
            have[gems[s]] = (cnt - 1, idx)
            if cnt == 1:
                visited[idx] = 0
            s += 1

    while sum(visited) == c:
        cnt, idx = have[gems[s]]
        if e - s < min_l:
            min_l = e - s
            answer = [s + 1, e]
        have[gems[s]] = (cnt - 1, idx)
        if cnt == 1:
            visited[idx] = 0
        s += 1

    return answer