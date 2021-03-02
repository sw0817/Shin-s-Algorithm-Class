# 백준 1327 소트 게임
# Baekjoon 1327

# Created by sw0817 on 2021. 03. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1327

from _collections import deque

def check():
    # 배열 사용여부를 검사할건데 방문배열이 아닌 set를 사용하기 위해 문자열로 치환
    string = "".join(array)
    used = set(string)

    # 큐
    queue = deque()
    queue.append(string)

    # 뒤집기 횟수
    cnt = -1

    while queue:

        # n번 뒤집기 경우의 수 모두 확인한 후 n+1번 뒤집기 경우의 수를 확인한다.
        cnt += 1

        # 위 조건을 위한 for문
        for _ in range(len(queue)):
            string = queue.popleft()
            cur_array = list(string)

            # 정답이면 현재 뒤집기 횟수가 답
            if cur_array == answer:
                return cnt

            # K개 숫자를 뒤집을 수 있는 모든 구간에 대해 뒤집어 본다.
            for i in range(N - K + 1):
                new_array = cur_array[:]
                reverse = new_array[i:i + K]
                reverse.reverse()

                for j in range(K):
                    new_array[i + j] = reverse[j]

                # 뒤집어서 만든 문자열이 처음 만든 문자열이면 큐에 추가
                new_string = "".join(new_array)
                if new_string not in used:
                    used.add(new_string)
                    queue.append(new_string)

    # 오름차순 못 만들면 -1이 답
    return -1


# 1~N 수 한 번에 K개 뒤집기
N, K = map(int, input().split())

# 일단 배열로 받는다.
array = list(input().split())

# 소팅한 결과가 오름차순
answer = sorted(array)

print(check())
