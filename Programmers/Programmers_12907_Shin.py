def solution(n, money):
    answer = [1] + [0] * n
    mod = 1000000007

    for m in money:
        for cur_n in range(m, n+1):
            if m <= cur_n:
                answer[cur_n] += answer[cur_n - m]
                answer[cur_n] %= mod

    return answer[n]