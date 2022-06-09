def toSec(m, s):
    return m * 60 + s


def solution(m, musicinfos):
    answer = []
    music_dict = {}
    t_m = ''
    l = len(m)
    idx = l - 1
    sharp = False
    while 0 <= idx:
        if m[idx] == '#':
            sharp = True
        else:
            if sharp:
                t_m += m[idx].lower()
            else:
                t_m += m[idx]
            sharp = False
        idx -= 1

    m = ''.join(reversed(list(t_m)))

    for i in range(len(musicinfos)):
        s, e, title, info = list(map(str, musicinfos[i].split(',')))
        l = len(info)
        t_info = ''
        idx = l - 1
        sharp = False
        while 0 <= idx:
            if info[idx] == '#':
                sharp = True
            else:
                if sharp:
                    t_info += info[idx].lower()
                else:
                    t_info += info[idx]
                sharp = False
            idx -= 1

        info = ''.join(reversed(list(t_info)))
        l = len(info)
        d = toSec(int(e[:2]), int(e[3:])) - toSec(int(s[:2]), int(s[3:]))

        if d <= l:
            info = info[:d]
        else:
            info = info * (d // l) + info[:l % d]

        if m in info:
            if title in music_dict:
                a, b, c = music_dict[title]
                music_dict[title] = [d + a, b, c]
            else:
                music_dict[title] = [d, i, title]

    for title in music_dict:
        answer.append(music_dict[title])

    answer.sort(key=lambda x: [-x[0], x[1]])

    return answer[0][2] if answer else '(None)'