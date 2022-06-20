Info = []
max_point = 0
last_info = ""

# 현재 맞출 점수, 현재 점수, 맞춘 정보, 남은 화살 수, 어피치점수
def check(idx, point, info, cnt, apeach):
    global max_point, last_info, Info

    # 모든 점수에 대해 조사했으면
    if idx == 11:
        # 라이언이 점수 더 높으면
        if apeach < point:
            # 점수 차이가 최대이면 갱신
            if max_point < point - apeach:
                max_point = point - apeach
                last_info = info
            # 점수 차이 같으면
            if max_point == point - apeach:
                # 낮은 점수 많이 맞춰야함
                for i in range(10, -1, -1):
                    # 많이 맞췄으면 갱신
                    if int(last_info[i]) < int(info[i]):
                        last_info = info
                        break
                    # 적게 맞췄으면 나가리
                    elif int(last_info[i]) > int(info[i]):
                        break
                    # 여기는 같은 경우
        return

    # 0점 짜리의 경우 남은 화살 다 쏘기
    if idx == 10:
        check(idx + 1, point, info + str(cnt), 0, apeach)
        return

    # 남은 화살이 어피치가 이번 점수 맞춘거보다 많으면
    if Info[idx] < cnt:
        # 한 발 더 쏨
        n = Info[idx] + 1
        # 어피치는 이번 점수 획득 못 함
        check(idx + 1, point + 10 - idx, info + str(n), cnt - n, apeach - (10 - idx))

    # 어피치도 여기 쏜게 없으면
    if not Info[idx]:
        # 점수 감점
        apeach -= 10 - idx

    # 이번 점수는 안 쏘고 넘어가기
    check(idx + 1, point, info + "0", cnt, apeach)


def solution(n, info):
    global last_info, Info

    Info = info

    # 시작은 어피치가 1~10 점 모두 가지고 있는 상태에서 시작
    check(0, 0, "", n, 55)
    answer = list(map(int, last_info))

    return answer if answer else [-1]