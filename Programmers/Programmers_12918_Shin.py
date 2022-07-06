def solution(s):
    try:
        a = int(s)
        if len(s) == 4 or len(s) == 6:
            return True
    except:
        return False
    return False