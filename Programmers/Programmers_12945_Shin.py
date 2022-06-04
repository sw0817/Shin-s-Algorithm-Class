def solution(n):
    mod = 1234567
    dp = [0] + [1] * n
    for i in range(2, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % mod

    return dp[n]