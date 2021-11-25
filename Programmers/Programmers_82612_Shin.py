def solution(price, money, count):
    answer = ((count * (count + 1)) // 2) * price - money
    return answer if 0 < answer else 0