from collections import deque

def solution(record):
    answer = []
    infos = deque()
    users = dict()

    for rec in record:
        rec = list(map(str, rec.split()))
        if len(rec) == 2:
            action, id = rec
        else:
            action, id, nick = rec
            users[id] = nick
        infos.append((action, id))

    for action, id in infos:
        act = ""
        if action == 'Enter':
            act = " 들어왔습니다."
        elif action == 'Leave':
            act = " 나갔습니다."
        else:
            continue
        answer.append(users[id] + "님이" + act)

    return answer