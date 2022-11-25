def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for w in words:
            if not w * 2 in bab:
                bab = bab.replace(w, " ")
        if not bab.replace(" ", ""):
            answer += 1

    return answer