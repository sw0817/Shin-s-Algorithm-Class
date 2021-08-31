def solution(new_id):
    # 모든 대문자를 소문자로 치환
    # 숫자, 빼기, 밑줄, 마침표 제외 모두 제거
    # 마침표 연속 시 하나로 치환
    # 처음이나 끝에 마침표 있으면 제거
    # 빈 문자열이면 "a" 대입
    # 길이가 16자 이상이면 첫 15자만 남기고, 마지막 문자가 마침표면 제거
    # 길이가 2자 이하이면 마지막 문자를 길이 3까지 반복
    renewal_id = ''
    tools = ['-', '.', '_']
    for t in new_id:
        if 65 <= ord(t) < 91:
            renewal_id += chr(ord(t) + 32)
        else:
            if 48 <= ord(t) <= 57 or 97 <= ord(t) < 123:
                renewal_id += t
            elif t in tools:
                if t == '.':
                    if not renewal_id or renewal_id[-1] == '.':
                        continue
                    else:
                        renewal_id += t
                else:
                    renewal_id += t

    if renewal_id:
        while renewal_id and renewal_id[-1] == '.':
            renewal_id = renewal_id[:-1]
    else:
        renewal_id = 'a'

    if 15 < len(renewal_id):
        renewal_id = renewal_id[:15]
        while renewal_id and renewal_id[-1] == '.':
            renewal_id = renewal_id[:-1]

    while len(renewal_id) < 3:
        renewal_id += renewal_id[-1]

    return renewal_id