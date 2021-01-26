# 백준 1992 쿼드트리
# Baekjoon 1992

# Created by sw0817 on 2021. 01. 26..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1992

# 재귀를 사용한다.
def quadTree(x1, y1, x2, y2):

    # x2 - x1 == 1이라면 검사하는 영상파일의 길이가 1이라는 의미이다.
    if x2 - x1 == 1:
        return video[y1][x1]

    # 쿼드 트리 형태로 계속해서 쪼갠다.
    quad1 = quadTree(x1, y1, (x1+x2)//2, (y1+y2)//2)
    quad2 = quadTree((x1+x2)//2, y1, x2, (y1+y2)//2)
    quad3 = quadTree(x1, (y1+y2)//2, (x1+x2)//2, y2)
    quad4 = quadTree((x1+x2)//2, (y1+y2)//2, x2, y2)

    # 쪼개진 네 조각이 같다면 그 파일 문자를 출력한다.

    ## len(quad1) == 1을 안 붙였었는데 이 경우
    # 4
    # 1010
    # 0000
    # 1010
    # 0000
    # 같은 케이스를 첫 네등분이 같아 쿼드트리가 만족한다고 판단한다.
    # 그러므로, 가장 작은 1크기부터 쿼드트리를 만족하는지 판단한다.

    if quad1 == quad2 == quad3 == quad4 and len(quad1) == 1:
        return quad1

    # 쪼개진 네 조각이 다르다면 괄호를 추가하고 다른 부분을 쪼개어 출력해야 한다.
    return "(" + quad1 + quad2 + quad3 + quad4 + ")"


N = int(input())
video = [input() for _ in range(N)]

# 리턴 되는 순서대로 출력한다.
print(quadTree(0, 0, N, N))

# 모두다 같은 숫자면 괄호없이 그 숫자 출력된다고 생각하고 제출해본다.
