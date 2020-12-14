# 1부터 num까지의 제곱ㄴㄴ수의 갯수를 리턴
def found(num):
    res = 0
    for i in range(1, int(num ** 0.5) + 1):
        res += mo[i] * (num // (i * i))
    return res


# 최대 인풋의 제곱근보다 큰 값
MAX = 200001

# 뫼비우스 배열
mo = [0] * MAX
mo[1] = 1

# 뫼비우스 값 갱신
for i in range(1,MAX):
    j = 2 * i
    while j < MAX:
        mo[j] -= mo[i]
        j += i

n = int(input())
left = 1
right = 20000000000

# 이분탐색
while left < right:
    mid = (left + right) // 2
    now = found(mid)
    if now < n:
        left = mid + 1
    elif now > n:
        right = mid - 1
    else:
        right = mid

# 정답출력
print(left)