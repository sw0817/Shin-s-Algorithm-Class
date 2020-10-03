# 백준 17135 찾기
# Baekjoon 17135

# Created by sw0817 on 2020. 10. 03..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/17135


import copy


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)] # M열
result = 0
# 궁수가 3명 이니까
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            arr2 = copy.deepcopy(arr)
            C1 = [0] * M
            # i, j, k 세 명의 궁수 배치가 가능하고
            C1[i] = C1[j] = C1[k] = 1
            # 그 배치를 성 위치에 추가
            arr2.append(C1)
            # 조합 별 제거하게 되는 병사 수
            cnt = 0
            # 궁수만 남을 때까지 병사가 한 줄씩 내려옴
            while len(arr2) != 1:
                # 쏠 병사 타겟 리스트
                targets = []
                for l in range(M):
                    # 궁수 위치에서
                    if arr2[-1][l] == 1:
                        # 현재 target 위치 초기화(M열은 없음 실제로)
                        target = [D+1, M, 0]
                        # 궁수 앞 행까지
                        for r in range(len(arr2)-2, -1, -1):
                            for c in range(M):
                                # 병사가 있고, 그 거리가 사거리 내라면
                                if arr2[r][c] == 1 and (abs(len(arr2)-1-r) + abs(l-c)) <= D:
                                    # 현재 target 보다 가까우면 target 변경
                                    if (abs(len(arr2)-1-r) + abs(l-c)) < target[0]:
                                        target = [(abs(len(arr2)-1-r) + abs(l-c)), c, r]
                                    # 거리가 같다면
                                    elif (abs(len(arr2)-1-r) + abs(l-c)) == target[0]:
                                        # 더 왼쪽일 때
                                        if c < target[1]:
                                            # target 변경
                                            target = [(abs(len(arr2)-1-r) + abs(l-c)), c, r]
                        # target 이 초기값이 아니라면(병사가 선택 되었으면)
                        if target != [D+1, M, 0]:
                            # target 리스트에 추가 (동시에 맞출수도 있으니 아직 쏘면 안 됨)
                            if not [target[1], target[2]] in targets:
                                targets.append([target[1], target[2]])
                # 병사들을 쏘아 0으로 갱신
                for o in range(len(targets)):
                    # targets 내 target[0] == 거리임
                    arr2[targets[o][1]][targets[o][0]] = 0
                    # 죽인 병사 수 추가
                    cnt += 1
                # 궁수 앞 행 제거(병사 한 줄 내려옴)
                arr2.pop(-2)
            # 이 조합으로 죽인 병사 수가 가능한 최대인지 체크
            if cnt > result:
                result = cnt

print(result)