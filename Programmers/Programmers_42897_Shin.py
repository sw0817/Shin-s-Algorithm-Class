def solution(money):
    l = len(money)

    money2 = money[1:]

    # 처음 사용
    dp1 = [money[0]] * (l-1)
    # 두 번째 사용
    dp2 = [money[1]] * (l-1)
    dp1[1] = max(money[0], money[1])
    dp2[1] = max(money2[0], money2[1])
    for i in range(2, l-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
        dp2[i] = max(dp2[i-1], dp2[i-2] + money2[i])

    return max(max(dp1), max(dp2))