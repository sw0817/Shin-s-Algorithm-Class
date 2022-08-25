import math

def solution(alp, cop, problems):
    A, C = 0, 0

    probs = []
    for a, c, ra, rc, cost in problems:
        if ra or rc:
            if cost < ra + rc:
                probs.append([a, c, ra, rc, cost])
        A = max(A, a)
        C = max(C, c)

    dp = [[math.inf] * (C + 1) for _ in range(A + 1)]

    alp = min(A, alp)
    cop = min(C, cop)

    dp[alp][cop] = 0
    for i in range(alp, A + 1):
        for j in range(cop, C + 1):
            for a, c, ra, rc, cost in probs:
                if a <= i and c <= j:
                    dp[min(i + ra, A)][min(j + rc, C)] = min(dp[min(i + ra, A)][min(j + rc, C)], dp[i][j] + cost)
            if i < A:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < C:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

    return dp[-1][-1]