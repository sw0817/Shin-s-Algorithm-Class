# SWEA 2063 중간값 찾기
# SWEA 2063

# Created by sw0817 on 2020. 09. 11..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QPsXKA2UDFAUq&categoryId=AV5QPsXKA2UDFAUq&categoryType=CODE


N = int(input())
nums = list(map(int, input().split()))
new_nums = sorted(nums)
print(new_nums[N//2])