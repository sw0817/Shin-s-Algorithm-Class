def solution(numbers):
    answer = []

    for n in numbers:
        if not n % 2:
            answer.append(n + 1)
        else:
            ans = n + (n ^ (n + 1) + 1) / 4
            if int(ans) < ans:
                ans = int(ans) + 1
            answer.append(ans)

    return answer