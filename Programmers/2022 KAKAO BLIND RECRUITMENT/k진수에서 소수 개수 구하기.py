def check(n):
    if n == 1:
        return
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return
    return True


def solution(n, k):
    answer = 0

    num = ''
    while k <= n:
        i = n % k
        num += str(i)
        n = n // k
    num += str(n % k)

    nums = list(map(str, ''.join(reversed(num)).split('0')))

    for num in nums:
        if num and check(int(num)):
            answer += 1

    return answer