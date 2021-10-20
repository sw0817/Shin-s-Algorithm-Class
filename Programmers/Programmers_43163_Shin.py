visited = []


def change(cur, words, cnt, l):
    global visited

    for i in range(len(words)):
        n = 0
        for j in range(l):
            if cur[j] != words[i][j]:
                n += 1
        if n == 1 and cnt + 1 < visited[i]:
            visited[i] = cnt + 1
            change(words[i], words, cnt + 1, l)


def solution(begin, target, words):
    global visited
    answer = 0
    l = len(words)
    visited = [987654321] * l

    change(begin, words, 0, len(words[0]))

    if not target in words or visited[words.index(target)] == 987654321:
        return 0

    return visited[words.index(target)]