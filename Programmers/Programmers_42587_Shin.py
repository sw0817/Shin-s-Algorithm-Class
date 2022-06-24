from collections import deque


def solution(priorities, location):
    answer = 0

    dic = dict()
    for i in range(1, 10):
        dic[i] = 0
    for p in priorities:
        dic[p] += 1

    queue = deque()

    for i in range(len(priorities)):
        queue.append((priorities[i], i))

    for i in range(9, 0, -1):
        while dic[i]:
            p, idx = queue.popleft()
            if p == i:
                dic[p] -= 1
                answer += 1
                if idx == location:
                    return answer
            else:
                queue.append((p, idx))