def solution(n, left, right):
    answer = []

    r1, r2, c1, c2 = left // n, right // n, left % n, right % n
    if r1 < r2:
        for j in range(c1, n):
            answer.append(max(r1, j) + 1)
        for i in range(r1+1, r2):
            for j in range(n):
                answer.append(max(i, j) + 1)
        for j in range(c2+1):
            answer.append(max(r2, j) + 1)
    else:
        for j in range(c1, c2+1):
            answer.append(max(r1, j) + 1)

    return answer