# SWEA 1267 작업 순서
# SWEA 1267

# Created by sw0817 on 2020. 10. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18TrIqIwUCFAZN&categoryId=AV18TrIqIwUCFAZN&categoryType=CODE


for tc in range(1, 11):
    # 입력 받아오기
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))

    # 인접리스트 작성
    r_list = [[] for _ in range(V+1)]
    # 각 작업 당 선행 작업 필요한 작업 리스트를 만든다
    for i in range(E):
        r_list[temp[i*2+1]].append(temp[i*2])

    # 결과 넣을 리스트 및 작업 체크
    result = []
    visited = [0] * (V+1)

    # 작업 다 하면 리스트 길이는 V
    while len(result) != V:
        # 모든 작업에 대해
        for i in range(1, V+1):
            # 작업 체크 되어 있으면 선행 작업 리스트에서 삭제
            for j in r_list[i]:
                if visited[j] == 1:
                    r_list[i].remove(j)
            # 아직 작업 체크 안했고 선행 작업 리스트가 비어 있으면 작업하기
            if len(r_list[i]) == 0 and visited[i] == 0:
                result.append(i)
                visited[i] = 1

    print('#{}'.format(tc), end=' ')
    print(*result)