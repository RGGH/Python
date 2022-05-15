# https://leetcode.com/problems/two-sum/

target = 0
nums = [1,3,0,0]


def fun(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]


print(fun(nums, target))
