from collections import deque


def solution(numbers, target):
    ret = 0
    queue = deque()
    queue.append(numbers[0])
    queue.append(-numbers[0])
    for i in range(1, len(numbers)):
        for _ in range(len(queue)):
            n = queue.popleft()
            queue.append(n + numbers[i])
            queue.append(n - numbers[i])

    while queue:
        n = queue.popleft()
        if n == target:
            ret += 1

    return ret