Money = 0
Stocks = []
Answer = 0
l = 0
dp = []

def recur(idx, cur_m, ret):
    global Money, Stocks, Answer, l, dp

    if idx == l:
        Answer = max(Answer, ret)
        return

    if ret <= dp[idx][cur_m]:
        return

    dp[idx][cur_m] = ret

    if Stocks[idx][1] <= cur_m:
        recur(idx + 1, cur_m - Stocks[idx][1], ret + Stocks[idx][0])
    recur(idx + 1, cur_m, ret)


def solution(money, stocks):
    global Money, Stocks, Answer, l, dp

    Money = money
    Stocks = stocks
    l = len(Stocks)
    dp = [[-1] * 100000 for _ in range(100)]

    recur(0, money, 0)

    return Answer