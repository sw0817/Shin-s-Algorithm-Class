def solution(msg):
    answer = []

    l = len(msg)
    ll = l
    idx = 0
    dic = {}
    for i in range(1, 27):
        dic[chr(i + 64)] = i

    nxt = 27
    word = msg[0]

    while idx < l:
        if word in dic:
            if idx == l - 1:
                answer.append(dic[word])
                nxt += 1
                break
            else:
                idx += 1
            word += msg[idx]
        else:
            dic[word] = nxt
            answer.append(dic[word[:-1]])
            nxt += 1
            word = msg[idx]

    return answer