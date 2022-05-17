def solution(s):
    s = list(map(str, s[2:-2].split('},{')))
    l = len(s)
    answer = [0] * l
    dic = dict()
    for tup in s:
        tup = list(map(int, tup.split(',')))
        for n in tup:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1

    for n in dic:
        answer[l - dic[n]] = n

    return answer