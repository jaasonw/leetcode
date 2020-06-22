# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.

# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _nums = {}
        for i in range(len(nums)):
            _nums[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in _nums and _nums[target - nums[i]] != i:
                return [i, _nums[target - nums[i]]]
        return []
