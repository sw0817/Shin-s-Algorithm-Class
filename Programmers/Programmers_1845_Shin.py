def solution(nums):
    l = len(nums) // 2
    nums = set(nums)

    return min(l, len(nums))