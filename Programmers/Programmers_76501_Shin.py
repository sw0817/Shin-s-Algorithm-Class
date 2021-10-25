def solution(absolutes, signs):
    answer = 0

    l = len(signs)

    for i in range(l):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer