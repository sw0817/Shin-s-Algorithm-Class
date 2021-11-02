def solution(genres, plays):
    answer = []

    l = len(plays)

    play_sum = dict()

    for i in range(l):
        if genres[i] in play_sum:
            play_sum[genres[i]] += plays[i]
        else:
            play_sum[genres[i]] = plays[i]

    play_list = []
    g_name = []
    for p in play_sum:
        play_list.append([play_sum[p], p])

    play_list.sort(reverse=True)

    for i in range(len(play_list)):
        g_name.append(play_list[i][1])

    result = []
    for i in range(l):
        result.append([g_name.index(genres[i]), plays[i], i])

    result.sort(key=lambda x: [x[0], -x[1], x[2]])
    cnt = dict()
    for i in range(l):
        if not result[i][0] in cnt:
            cnt[result[i][0]] = 1
        else:
            if cnt[result[i][0]] == 2:
                continue
            else:
                cnt[result[i][0]] += 1
        answer.append(result[i][2])

    return answer