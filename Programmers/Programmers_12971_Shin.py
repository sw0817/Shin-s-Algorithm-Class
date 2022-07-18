def solution(sticker):
    l = len(sticker)
    if l <= 2:
        return max(sticker)

    sticker2 = sticker[1:]

    # 처음 사용
    dp1 = [sticker[0]] * (l-1)
    # 두 번째 사용
    dp2 = [sticker[1]] * (l-1)
    dp1[1] = max(sticker[0], sticker[1])
    dp2[1] = max(sticker2[0], sticker2[1])
    for i in range(2, l - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker2[i])

    return max(max(dp1), max(dp2))