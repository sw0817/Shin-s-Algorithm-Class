def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        if budget < d[i]:
            return i
        budget -= d[i]

    return len(d)