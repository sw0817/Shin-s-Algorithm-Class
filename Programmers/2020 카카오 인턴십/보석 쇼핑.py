def solution(gems):
    names = list(set(gems))
    have = dict()
    c = len(names)
    l = len(gems)
    if c == 1:
        return [1, 1]
    answer = [1, l]
    min_l = l
    s, e = 0, 0
    have[gems[e]] = 1
    e += 1
    while e < l:
        if len(have) != c:
            if gems[e] in have:
                have[gems[e]] += 1
            else:
                have[gems[e]] = 1
            e += 1
        else:
            if e - s < min_l:
                min_l = e - s
                answer = [s + 1, e]
            if have[gems[s]] == 1:
                del have[gems[s]]
            else:
                have[gems[s]] -= 1
            s += 1

    while len(have) == c:
        if e - s < min_l:
            min_l = e - s
            answer = [s + 1, e]

        if have[gems[s]] == 1:
            del have[gems[s]]
        else:
            have[gems[s]] -= 1
        s += 1

    return answer