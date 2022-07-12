def solution(land):
    r = len(land)
    c = len(land[0])
    dp = [[0] * c for _ in range(r + 1)]

    for i in range(1, r + 1):
        for j in range(c):
            dp[i][j] = max(dp[i - 1][:j] + dp[i - 1][j + 1:]) + land[i - 1][j]

    return max(dp[r])