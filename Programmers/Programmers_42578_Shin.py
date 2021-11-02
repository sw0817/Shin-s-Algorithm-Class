def solution(clothes):
    answer = 1

    info = dict()

    for cloth in clothes:
        if cloth[1] in info:
            info[cloth[1]] += 1
        else:
            info[cloth[1]] = 2

    for cloth in info:
        answer *= info[cloth]

    return answer - 1