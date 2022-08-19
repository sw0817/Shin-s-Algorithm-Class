def solution(survey, choices):
    answer = ''

    types = ['RT', 'CF', 'JM', 'AN']
    point = dict()
    for t in types:
        for alp in t:
            point[alp] = 0

    for i in range(len(survey)):
        p = choices[i]
        if p < 4:
            point[survey[i][0]] += abs(p - 4)
        elif 4 < p:
            point[survey[i][1]] += abs(p - 4)

    for t in types:
        if point[t[0]] < point[t[1]]:
            answer += t[1]
        else:
            answer += t[0]

    return answer