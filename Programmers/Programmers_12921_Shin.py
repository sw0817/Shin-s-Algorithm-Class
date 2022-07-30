def solution(n):
    nums = [1] * (n + 1)

    for i in range(2, n+1):
        if nums[i]:
            for j in range(i*2, n+1, i):
                nums[j] = 0

    return  sum(nums[2:])