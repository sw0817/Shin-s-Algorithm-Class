import sys

sys.setrecursionlimit(200001)
rooms = dict()

def solution(k, room_number):
    global rooms

    for r in room_number:
        check(r)

    return list(rooms.keys())


def check(r):
    global rooms

    if r not in rooms:
        rooms[r] = r + 1
        return r

    nxt = check(rooms[r])
    rooms[r] = nxt + 1

    return nxt