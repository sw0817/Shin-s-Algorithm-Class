def solution(n):
    answer = []

    n = str(n)
    l = len(n)
    for i in range(l - 1, -1, -1):
        answer.append(int(n[i]))

    return answer