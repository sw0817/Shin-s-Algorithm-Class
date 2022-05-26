def solution(board, skill):
    answer = 0

    N = len(board)
    M = len(board[0])

    ds = [0, 1, -1]

    skill_sum = [[0] * (M + 1) for _ in range(N + 1)]
    for t, r1, c1, r2, c2, d in skill:
        skill_sum[r1][c1] -= d * ds[t]
        skill_sum[r1][c2 + 1] += d * ds[t]
        skill_sum[r2 + 1][c1] += d * ds[t]
        skill_sum[r2 + 1][c2 + 1] -= d * ds[t]

    for i in range(N + 1):
        for j in range(1, M + 1):
            skill_sum[i][j] += skill_sum[i][j - 1]

    for j in range(M + 1):
        for i in range(1, N + 1):
            skill_sum[i][j] += skill_sum[i - 1][j]

    new_board = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            new_board[i][j] = board[i][j] + skill_sum[i][j]
            if 0 < board[i][j] + skill_sum[i][j]:
                answer += 1

    return answer