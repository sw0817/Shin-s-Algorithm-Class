def solution(str1, str2):
    dict1 = dict()
    dict2 = dict()

    for i in range(len(str1) - 1):
        if 97 <= ord(str1[i]) <= 122 or 65 <= ord(str1[i]) <= 90:
            if 97 <= ord(str1[i + 1]) <= 122 or 65 <= ord(str1[i + 1]) <= 90:
                cur = str1[i].lower() + str1[i + 1].lower()
                if cur in dict1:
                    dict1[cur] += 1
                else:
                    dict1[cur] = 1

    for i in range(len(str2) - 1):
        if 97 <= ord(str2[i]) <= 122 or 65 <= ord(str2[i]) <= 90:
            if 97 <= ord(str2[i + 1]) <= 122 or 65 <= ord(str2[i + 1]) <= 90:
                cur = str2[i].lower() + str2[i + 1].lower()
                if cur in dict2:
                    dict2[cur] += 1
                else:
                    dict2[cur] = 1

    words = set(dict1) | set(dict2)
    if not words:
        return 65536

    min_ = 0
    max_ = 0
    for word in words:
        if not word in dict1:
            max_ += dict2[word]
        elif not word in dict2:
            max_ += dict1[word]
        else:
            min_ += min(dict1[word], dict2[word])
            max_ += max(dict1[word], dict2[word])

    answer = int(min_ / max_ * 65536)

    return answer