def solution(left, right):
    answer = 0

    for n in range(left, right + 1):
        cnt = 0
        for i in range(1, int(n ** 0.5) + 1):
            if not n % i:
                if n // i == i:
                    cnt += 1
                else:
                    cnt += 2

        if cnt % 2:
            answer -= n
        else:
            answer += n

    return answer