def solution(citations):
    answer = 0

    citations.sort(reverse=True)
    l = len(citations)

    for i in range(l):
        cnt = citations[i]
        if i + 1 <= cnt:
            answer = max(answer, i + 1)

    return answer