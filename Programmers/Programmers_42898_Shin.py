def solution(m, n, puddles):
    answer = 0

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for c, r in puddles:
        dp[r - 1][c - 1] = -1

    for i in range(1, n):
        if dp[i][0] == 0:
            dp[i][0] += 1
        else:
            break

    for j in range(1, m):
        if dp[0][j] == 0:
            dp[0][j] += 1
        else:
            break

    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] != -1:
                if dp[i][j - 1] != -1:
                    dp[i][j] += dp[i][j - 1] % 1000000007
                if dp[i - 1][j] != -1:
                    dp[i][j] += dp[i - 1][j] % 1000000007
                dp[i][j] %= 1000000007

    return dp[n - 1][m - 1] % 1000000007