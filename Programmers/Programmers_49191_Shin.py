def solution(n, results):
    answer = 0

    win = [set() for _ in range(n + 1)]
    lose = [set() for _ in range(n + 1)]

    for a, b in results:
        win[a].add(b)
        win[a] |= win[b]
        lose[b].add(a)
        lose[b] |= lose[a]

    for i in range(1, n + 1):
        for b in win[i]:
            lose[b] |= lose[i]
        for b in lose[i]:
            win[b] |= win[i]

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer