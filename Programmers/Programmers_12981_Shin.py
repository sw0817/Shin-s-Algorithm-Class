def solution(n, words):
    used = set()
    last_alp = words[0][0]
    for i in range(len(words)):
        word = words[i]
        if word[0] != last_alp or word in used:
            return [i % n + 1, i // n + 1]
        used.add(word)
        last_alp = word[-1]

    return [0, 0]