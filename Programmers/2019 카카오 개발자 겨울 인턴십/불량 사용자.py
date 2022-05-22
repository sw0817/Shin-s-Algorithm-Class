from itertools import permutations


def solution(user_id, banned_id):
    answer = set()
    cnt = len(banned_id)
    for perm in permutations(user_id, cnt):
        yn = True
        for i in range(cnt):
            l = len(banned_id[i])
            if len(perm[i]) != l:
                yn = False
                break
            for j in range(l):
                if banned_id[i][j] == '*' or banned_id[i][j] == perm[i][j]:
                    continue
                else:
                    yn = False
                    break

        if yn:
            answer.add(tuple(sorted(list(perm))))

    return len(answer)