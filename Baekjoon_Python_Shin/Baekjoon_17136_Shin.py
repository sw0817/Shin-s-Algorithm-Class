# 백준 17136 색종이 붙이기
# Baekjoon 17136

# Created by sw0817 on 2020. 10. 05..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/17136


# 종이 붙여보자
def attach(n, cnt):
    global result
    # 다 붙였으면
    if cnt == 0:
        # 사용한 종이 수가 최소다
        if n < result:
            # 갱신
            result = n
    # 최소보다 종이 이미 더 사용 ?
    elif n >= result:
        # 나가리
        return
    # 남은 종이가 없다
    elif sum(cnts) == 0:
        # 나가리
        return
    # 그게 아니면 시작하거나 재귀해 ~
    else:
        for i in range(10):
            for j in range(10):
                # 종이 붙여야하고 아직 안 붙였으면 (이 부분이 붙여야 하는 최상단 좌측)
                if paper[i][j] == 1 and visited[i][j] == 0:
                    # 큰 종이부터 붙여본다
                    for k in range(5, 0, -1):
                        # 해당 크기 종이가 남아 있고, 종이 붙여도 배열 안 넘어가면
                        if cnts[k-1] > 0 and i+k <= 10 and j+k <= 10:
                            # 붙여야 하는 1이 몇 개인지 체크
                            ones = 0
                            # 해당 크기 종이 붙는 범위에서
                            for l in range(i, i+k):
                                for o in range(j, j+k):
                                    # 종이 안 붙였고 붙여야 하는 자리 크기 체크
                                    if visited[l][o] == 0 and paper[l][o] == 1:
                                        ones += 1
                            # 그 크기가 종이 크기랑 같다 ?
                            if ones == k ** 2:
                                # 바로 붙여버려
                                for l in range(i, i + k):
                                    for o in range(j, j + k):
                                        visited[l][o] = 1
                                # 해당 크기 종이 사용했음 ㅇㅇ
                                cnts[k-1] -= 1
                                # 종이 하나 사용했고 붙여야 할 자리는 그만큼 줄었음 재귀
                                attach(n+1, cnt - ones)
                                # for 문으로 다른 크기 종이도 써봐야 하니까
                                for l in range(i, i + k):
                                    for o in range(j, j + k):
                                        # 다시 초기화
                                        visited[l][o] = 0
                                # 종이도 안 쓴걸로 해
                                cnts[k-1] += 1
                    # 모든 크기 종이 사용해봤으니 return
                    return


paper = [list(map(int, input().split())) for _ in range(10)]
# 크기별 종이 갯수 리스트
cnts = [5] * 5
visited = [[0] * 10 for _ in range(10)]
# 최대 종이 사용 갯수
result = 25
# 종이 붙여야 할 범위 크기의 합
cnt = 0
for i in range(10):
    for j in range(10):
        if paper[i][j] == 1:
            cnt += 1
attach(0, cnt)
# result 가 이따구면
if result == 25:
    # 다 붙인 케이스가 없네
    print(-1)
# 잘 구했으면
else:
    # 출력해라
    print(result)
