def solution(prices):
    l = len(prices)
    answer = [i for i in range(l-1, -1, -1)]
    stack = []
    for i in range(l):
        if not stack:
            stack.append([prices[i], i])
        else:
            while stack and stack[-1][0] > prices[i]:
                idx = stack.pop(-1)[1]
                answer[idx] = i - idx
            stack.append([prices[i], i])

    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))