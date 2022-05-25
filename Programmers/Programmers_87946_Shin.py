from itertools import permutations


def solution(k, dungeons):
    answer = -1
    l = len(dungeons)

    for perm in permutations(dungeons, l):
        cur = k
        for i in range(l):
            if perm[i][0] <= cur:
                cur -= perm[i][1]
                answer = max(answer, i + 1)
            else:
                break

    return answer